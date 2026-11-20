# 7. Pesquisa nas IAs (linha de base e comparação)

Objetivo: saber se e como o cliente aparece quando as pessoas perguntam a assistentes de IA, antes e depois do trabalho no perfil.

## Princípio

Fazer como uma pessoa faria: abrir o navegador, entrar na conta, digitar as perguntas e documentar as respostas. Não usar API para esta pesquisa, porque APIs podem devolver respostas diferentes das que o usuário vê.

Plataformas: ChatGPT, Gemini e Google AI Overview (a visão geral de IA da busca do Google).

## Quando rodar

- **Linha de base:** antes de criar ou otimizar o perfil.
- **Comparações:** 30, 60 e 90 dias depois.

## Conjunto fixo de perguntas

Monte de 8 a 15 perguntas por cliente, escritas como frases naturais, partindo da pesquisa de termos (`02-pesquisa-de-termos.md`). Tipos:

- Serviço e cidade: "quem faz [serviço] em [cidade]?"
- Serviço e situação: "qual o melhor [profissional] para [situação] em [cidade]?"
- Bairro ou região: "[serviço] perto de [bairro]".
- Nome do cliente: "quem é [nome]?" e "[nome] é boa [profissão]?"
- Nome do negócio, se houver.

Use as mesmas perguntas em todas as rodadas, para a comparação valer.

## Como rodar

1. Use contas logadas de forma consistente. Registre qual conta foi usada.
2. Faça cada pergunta em conversa nova.
3. Repita cada pergunta algumas vezes (por exemplo, 3), porque as respostas variam.
4. Para o Google, registre se o AI Overview apareceu e o que citou.
5. Copie a resposta e as fontes citadas.
6. Anote: o nome do cliente aparece? O perfil do Google é citado? Quais concorrentes aparecem?

Registre em `templates/registro-pesquisa-ias.csv`.

## Ressalvas

- As respostas variam entre rodadas, contas, locais e dias.
- Não existe API para AI Overviews, então a coleta é manual.
- Respeite os termos de uso de cada plataforma.
- Mudança depois do trabalho é correlação e não prova de que o perfil causou o resultado.
- Divulgar números em cases só com consentimento do cliente, sem prometer resultado.
