---
name: perfil-google-empresas
description: Criar ou otimizar o perfil de um cliente no Google Empresas (Google Business Profile): elegibilidade, pesquisa de termos, planejamento, preenchimento, verificação, gerência, avaliações e pesquisa nas IAs.
---

# Perfil no Google Empresas para clientes

Processo para agências e profissionais que montam perfis para clientes. Três camadas, que não se misturam:

1. **Regras do Google**: valem para todo caso. Conferir na ajuda oficial (support.google.com/business) antes de afirmar, porque mudam.
2. **Decisões por cliente**: apresentar opções e critérios. Quem decide é o cliente. Nunca copiar a decisão de outro caso.
3. **Fluxo da agência**: sugestão de ordem de trabalho. Cada agência adapta (ex.: onboarding por call, formulário ou e-mail). O que importa é o conjunto de dados coletados no fim, não o jeito de coletar.

Exemplos de caso (anonimizados), só para ilustrar: uma agência híbrida (atende online e presencial) com endereço oculto e área de atendimento; uma profissional autônoma que atende em salão de terceiros, somente com hora marcada. Não são padrão. Ver `docs/exemplos/`.

## 1. Elegibilidade

- Regra do Google: o negócio precisa ter contato presencial com clientes nos horários informados. Pode ser no local (endereço visível) ou indo até o cliente (área de atendimento, endereço oculto).
- **Negócio 100% online, sem nenhum contato presencial, não é elegível.** Se o negócio é majoritariamente online mas também atende presencialmente (grava, visita, recebe), ele pode ser elegível como negócio com área de atendimento, sem exibir endereço. Perguntar ao cliente qual é a realidade e não forçar.
- Também são inelegíveis: marcas, organizações, artistas, intermediários de leads, e serviço ou aula em local que o cliente não possui nem tem autoridade para representar.
- Local de terceiros (ex.: salão): exigir autorização do dono do local e não reivindicar nem alterar a ficha existente dele.
- Antes de criar: buscar no Maps se já existe perfil do cliente, para evitar duplicado.

## 2. Pesquisa de termos e benchmarks (antes de nome e descrições)

SEO e GEO (busca em IAs) pesam muito neste perfil. A pesquisa vem **antes** de escolher o nome e escrever descrições e serviços, e é a base deles. Detalhe em `docs/02-pesquisa-de-termos.md`.

- **Use os termos que o público realmente usa, não o vocabulário interno do negócio.** Muitas vezes o cliente chama o serviço de um jeito e quem pesquisa usa outro. Se o termo do negócio não aparece na busca real, não é ele que vai no perfil.
- **Buscas no Google:** autocomplete (com IP e cidade do cliente), buscas relacionadas, "as pessoas também perguntam", resultados do Maps. Anotar data e local.
- **Buscas em IAs:** aqui as pessoas escrevem **frases e perguntas inteiras**, não palavras soltas. Coletar as frases (ex.: "quem faz X em cidade para Y") e responder a elas na descrição e nos serviços, em linguagem natural.
- **Benchmark:** olhar perfis de concorrentes bem posicionados na mesma cidade: nome, categoria primária e secundárias, descrição, serviços, fotos, avaliações e o que as avaliações citam. Estudar, não copiar.
- **Saída da pesquisa:** lista de termos e frases reais, com observação de volume ou frequência quando houver, e o que ficou de fora por não ser usado pelo público. Isso alimenta categoria, nome (dentro das regras do Google), descrição, nomes e descrições de serviços e perguntas para avaliações.

## 3. Verificação (nem todo caso pede vídeo)

O Google decide quais métodos oferecer, conforme categoria, informações públicas, região e demanda, e pode exigir mais de um. Métodos possíveis: telefone ou SMS, e-mail, gravação de vídeo, videochamada ao vivo com o suporte, cartão postal (cada vez mais raro) e verificação instantânea (ex.: por Search Console). Só dá para saber quais aparecem ao chegar na etapa de verificação. Não prometer ao cliente um método. Detalhe em `docs/04-verificacao.md`.

| Cenário | O que fazer |
| --- | --- |
| Vídeo gravado | O cliente grava com o celular, no endereço, sem vídeo pré-gravado e sem documentos que não sejam do negócio. Mostrar local, sinalização ou entrada, e provas de que gerencia o negócio. Deixar para o fim, depois do perfil preenchido. |
| Videochamada | Mesmo cuidado de estar no local, com o cliente presente. |
| Telefone ou SMS | O número do perfil precisa receber ligação ou SMS. Atendimento automático (URA) não recebe o código. |
| E-mail | Código vai para o e-mail mostrado na tela, que o cliente acessa. |
| Cartão postal | Chega ao endereço, leva dias. Avisar o cliente para guardar. |
| Instantânea | Raramente disponível. Não contar com ela. |
| Mais de um método | Possível. Combinar com o cliente que ele pode ser acionado de novo. |
| Reprovação ou suspensão | Não recriar sem entender o motivo. Corrigir inconsistências (nome, endereço, categoria) e reenviar. |

## 4. Acesso e gerência

Detalhe em `docs/05-acesso-e-gerencia.md`.

- Um único proprietário principal, transferível. Recomendado: o cliente é proprietário e a agência é gerente.
- Gerente só pode ser adicionado depois que o perfil existe (confirmar na prática se o Google permite antes ou depois da verificação).
- **Se o cliente não quer compartilhar credenciais:** ele cria ou loga na própria conta, e a agência orienta ou conduz numa call. Depois do perfil criado, convida a agência como gerente.
- **Se o cliente aceita compartilhar credenciais:** a agência cria e preenche pela conta dele. Mesmo assim, convém a agência virar gerente ao final, para que o acesso contínuo não dependa de senha compartilhada. O cliente troca a senha logo depois. Pode haver pedido de código no celular dele ao logar em dispositivo novo.
- Nunca digitar senhas do cliente por ele. Nunca contornar CAPTCHA.
- Preferir que o perfil nasça no e-mail do cliente, para não ter que transferir depois.

## 5. Decisões por cliente (opções e critérios)

| Decisão | Opções | Critério |
| --- | --- | --- |
| Endereço | Visível ou oculto | Recebe clientes no local? Privacidade? |
| Horário com hora marcada | Listar horário com texto claro, ou não listar | Listar ajuda no ranking e no status aberto ou fechado, mas pode gerar visita sem agendar. Não existe opção própria para "somente com agendamento"; dizer na descrição e nos serviços. |
| Preço | Por serviço, "a partir de", ou sem preço | Política comercial do cliente |
| Site | Link, ou sem site | Se não há site, não inventar; planejar o link depois |
| Nome do perfil | Nome real do negócio, sem palavras-chave extras | Decidido a partir da pesquisa da seção 2, dentro do que o Google não derruba |
| Acesso | Ver seção 4 | Conforto do cliente |
| Contrato | Contrato, ou autorização registrada por escrito | Ver seção 9 |

## 6. Fluxo sugerido (adaptável)

1. **Coleta de informações** do cliente, do jeito que a agência preferir. Dados mínimos em `docs/01-coleta-de-informacoes.md`.
2. **Pesquisa de termos e benchmarks** (seção 2).
3. **Planejamento**: dossiê, posicionamento, estratégia do nome, checagem de perfil existente ou duplicado, decisões da seção 5.
4. **Linha de base nas IAs** (seção 8), antes de criar ou otimizar.
5. **Material visual**: pedir logo, capa e fotos (`docs/03-fotos.md`). Confirmar as medidas oficiais atuais antes de fixar.
6. **Login e preenchimento**: categoria, descrição, serviços com descrição, horários, contato, redes e fotos. Verificação por último.
7. **Orientação da verificação** conforme o método oferecido (seção 3).
8. **Gerência** (seção 4).
9. **Avaliações**: material com formas éticas de pedir comentários (`docs/06-avaliacoes.md`). Sem comprar, sem trocar por benefício, sem escrever pelo cliente.
10. **Repetir a pesquisa nas IAs** em 30, 60 e 90 dias.

## 7. Armadilhas de execução no navegador

Detalhe em `docs/08-playbook-navegador.md`.

- Conferir em qual conta Google está logado antes de criar.
- O formulário de endereço muda de layout ao escolher o estado: revisar bairro e linha 2 por captura de tela.
- Cuidado com o botão Cancelar ao salvar horários.
- Para serviços, navegar pela URL de edição em vez de clicar em Editar serviços.

## 8. Pesquisa nas IAs (linha de base e comparação)

Detalhe em `docs/07-pesquisa-nas-ias.md`.

- Feita como humano, no navegador, logado, sem API (APIs podem mascarar o resultado), em ChatGPT, Gemini e Google AI Overview.
- Conjunto fixo de perguntas por cliente, escritas como frases naturais (serviço + cidade, nome do profissional, "quem é o melhor X em cidade"), partindo da pesquisa da seção 2.
- Rodar mais de uma vez, registrar a resposta e as fontes citadas, e anotar se o nome aparece.
- Ressalvas: respostas variam, não há API para AI Overviews, respeitar termos de uso, resultado é correlação e não prova, e usar números em cases só com consentimento do cliente.

## 9. Autorizações e contrato

Checklist em `docs/09-contrato-checklist.md`. Cobrir: gerente e não proprietário, credencial temporária, métricas (LGPD), imagens, uso de resultados em cases sem promessa, responsabilidades do cliente (vídeo, estar no endereço, autorização do dono do local), elegibilidade e que a aprovação é decisão do Google, hora marcada, preço, pesquisa nas IAs e encerramento do acesso. Sem contrato formal, registrar a liberação por mensagem.

## 10. Escrita por canal

As regras de escrita mudam por canal. Não aplicar as do site ou das redes ao perfil sem checar.

- **Perfil no Google:** linguagem natural, com os termos e frases reais da pesquisa (seção 2), sem empilhar palavras-chave, sem promessa de resultado, dentro dos limites de caracteres e das regras de conteúdo do Google.
- **Outros canais (site, Instagram, anúncios):** seguir o guia de voz da marca de cada cliente ou agência. Definir esse guia antes de escrever.
