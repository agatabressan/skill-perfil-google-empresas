# 3. Fotos, logo e capa

## Especificações oficiais do Google (conferir antes de fixar)

Segundo a ajuda oficial do Google (support.google.com/business/answer/6103862, consultado em 19/11/2026):

- **Fotos:** formato JPG ou PNG, tamanho de 10 KB a 5 MB, resolução recomendada de 720 x 720 px e mínima de 250 x 250 px. Devem ser nítidas e bem iluminadas, sem edições pesadas ou filtros fortes.
- **Vídeos:** até 30 segundos, até 75 MB, 720p ou mais.
- **Logo e capa:** a página não traz especificações separadas. O logo aparece quando o perfil tem as informações básicas, como telefone e horário. A capa pode não ser exibida como primeira imagem.

Valores acima do mínimo funcionam bem. Referência usada em um caso anterior: logo 1200 x 1200 e capa 1920 x 1080, em JPG. É uma escolha de qualidade, não uma exigência do Google.

## O que pedir ao cliente

- Logo em alta resolução, de preferência quadrado e com área de respiro.
- Capa horizontal, sem texto importante nas bordas.
- Fotos reais do local (fachada ou entrada, interior), da equipe ou profissional, dos serviços em andamento e dos resultados.
- Evitar fotos com banco de imagem, com muito texto ou muito filtradas.

## Roteiro de fotos

1. Entrada ou fachada, para o cliente se reconhecer ao chegar.
2. Interior, ambiente de atendimento.
3. Profissional ou equipe.
4. Serviços sendo feitos.
5. Resultados, com consentimento de imagem quando houver pessoas.
6. Detalhes que mostram o cuidado do negócio.

## Consentimento

Fotos de clientes finais, inclusive antes e depois, só com consentimento de imagem por escrito.

## Tratamento leve (opcional)

Edição não é padrão. Quando necessário, use `tools/fotos/grade.py` para um ajuste leve de balanço de branco e contraste, e exporte os tamanhos. Não altere a realidade do local, porque o Google pede imagens fiéis.

Exemplo:

```bash
python tools/fotos/grade.py --entrada fotos-clientes/cliente-x --saida saida/cliente-x \
  --capa foto-capa.jpg --logo logo.png
```
