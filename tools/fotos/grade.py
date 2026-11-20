"""Tratamento leve de fotos para perfis no Google Empresas.

Faz balanço de branco parcial, corte de calor opcional, níveis, sombras e
contraste suaves. Exporta fotos, uma capa 16:9 e logos quadrados.

Uso:
    python tools/fotos/grade.py --entrada pasta/fotos --saida pasta/saida \
        [--capa foto.jpg] [--logo logo.png ...]

Não altere a realidade do local: o Google pede imagens fiéis.
Requer: pillow, numpy.
"""
import argparse
import os
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance

EXTENSOES = {".jpg", ".jpeg", ".png"}


def grade(im, wb=0.5, sat=1.0, shadow_lift=0.06, contrast=0.10, warm_cut=0.0):
    a = np.asarray(im).astype(np.float32) / 255.0
    # balanço de branco parcial (gray-world, com força limitada)
    m = a.reshape(-1, 3).mean(0)
    g = m.mean()
    gain = 1 + wb * ((g / m) - 1)
    gain = np.clip(gain, 0.88, 1.12)
    a = np.clip(a * gain, 0, 1)
    # corte extra de calor (laranja)
    if warm_cut:
        a[..., 0] *= 1 - warm_cut
        a[..., 2] *= 1 + warm_cut * 0.8
        a = np.clip(a, 0, 1)
    # níveis: estica só as pontas
    lo, hi = np.percentile(a, 0.4), np.percentile(a, 99.7)
    a = np.clip((a - lo) / (hi - lo + 1e-6), 0, 1)
    # levanta sombras de leve
    a = a + shadow_lift * (1 - a) ** 3
    # curva S suave
    s = a * a * (3 - 2 * a)
    a = (1 - contrast) * a + contrast * s
    out = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
    return ImageEnhance.Color(out).enhance(sat)


def salvar(im, destino: Path, lado_maior=2400, qualidade=88):
    im = im.copy()
    im.thumbnail((lado_maior, lado_maior), Image.LANCZOS)
    im.save(destino, quality=qualidade, optimize=True, progressive=True)
    print(destino.name, im.size, round(os.path.getsize(destino) / 1024), "KB")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--entrada", required=True, type=Path, help="pasta com as fotos")
    p.add_argument("--saida", required=True, type=Path, help="pasta de saída")
    p.add_argument("--capa", type=Path, help="foto para recortar em 16:9 (1920x1080)")
    p.add_argument("--logo", type=Path, nargs="*", default=[], help="logos a exportar em 1200x1200 (JPG)")
    p.add_argument("--wb", type=float, default=0.5, help="força do balanço de branco (0 a 1)")
    p.add_argument("--sat", type=float, default=0.97, help="saturação (1 = original)")
    p.add_argument("--shadow-lift", type=float, default=0.06)
    p.add_argument("--contrast", type=float, default=0.08)
    p.add_argument("--warm-cut", type=float, default=0.0, help="reduz tom alaranjado")
    p.add_argument("--lado-maior", type=int, default=2400)
    args = p.parse_args()

    args.saida.mkdir(parents=True, exist_ok=True)
    cfg = dict(wb=args.wb, sat=args.sat, shadow_lift=args.shadow_lift,
               contrast=args.contrast, warm_cut=args.warm_cut)

    for f in sorted(args.entrada.iterdir()):
        if f.suffix.lower() in EXTENSOES and f != args.capa:
            im = Image.open(f).convert("RGB")
            salvar(grade(im, **cfg), args.saida / (f.stem + ".jpg"), args.lado_maior)

    if args.capa:
        im = Image.open(args.capa).convert("RGB")
        w, h = im.size
        ch = int(w * 9 / 16)
        if ch > h:  # imagem mais larga que 16:9: corta nas laterais
            cw = int(h * 16 / 9)
            left = (w - cw) // 2
            cov = im.crop((left, 0, left + cw, h))
        else:  # recorta do rodapé para cima
            cov = im.crop((0, h - ch, w, h))
        cov = grade(cov, **cfg).resize((1920, 1080), Image.LANCZOS)
        destino = args.saida / "capa.jpg"
        cov.save(destino, quality=90, optimize=True, progressive=True)
        print("capa", cov.size, round(os.path.getsize(destino) / 1024), "KB")

    for logo in args.logo:
        l = Image.open(logo).convert("RGB").resize((1200, 1200), Image.LANCZOS)
        destino = args.saida / (logo.stem + "-1200.jpg")
        l.save(destino, quality=92, optimize=True)
        print(destino.name, l.size, round(os.path.getsize(destino) / 1024), "KB")


if __name__ == "__main__":
    main()
