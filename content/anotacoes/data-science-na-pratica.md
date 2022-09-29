---
title: "Data Science na Prática 3.0"
date: 2022-09-29T08:13:55-03:00
---


[Curso](https://escola.sigmoidal.ai/curso-data-science-na-pratica/)



## Decisões baseadas em Dados


### O que é Data Science (de verdade)

- Ciência envolve outras etapas além de programação/ML/modelagem. Ciência envolve você entender o problema;
- Etapas
    1. Defina o objetivo da pesquisa
    2. Faça uma hipótese
    3. Coleta de dados
    4. Teste sua hipótese
    5. Analise seus resultados
    6. Chegue a uma conclusão
    7. Refine a hipótese e repita
- Auxílio ao processo de tomada de decisão - Data-Driven


### ****Pensamento Analítico de Dados e Data Driven Decisions****

- Livro: [Data Science para Negócios](https://www.amazon.com.br/dp/8576089726/ref=cm_sw_r_tw_dp_6NPXZQ3VM4DQ10CPH5C5?_encoding=UTF8&psc=1)
- As pessoas querem “One Big Idea” para apresentar o resultado do trabalho
- Data → Information → Knowledge → Vantagem estratégica


### ****Senso Comum vs. Pensamento Científico****

- Livro: Metodologia de Pesquisa em Engenharia de Produção e Gestão de Operações
- Etapas
    1. Identificar o problema
    2. Obter informações sobre o problema
    3. Consultar referências
    4. Levantar hipóteses
    5. Validar hipóteses
    6. Entregável - relatório/dashboard/post
- Problema → Método → Solução → Aplicação → Conhecimento
- “A ciência é uma metamorfose do senso comum. Sem ele, ela não pode existir”
- A diferença é o Rigor



## Análise de Dados e Pandas

- [Anotações: Jupyter](/anotacoes/jupyter/)
- [Anotações: Python - pandas](/anotacoes/python/#pandas)


### ****Visualizando dados****

- [Interpretação de um histrograma](https://www.youtube.com/watch?v=L0f8d3B8dk4)
- gráfico de dispersão: bom para visualizar co-relação


### ****Lidando com valores ausentes****

- excluir
    - joga fora outros valores que seriam uteis
    - se o dataset for grande com poucos ausentes, talvez não tenha problema
- preencher
    - média ou mediana
        - mediana exclui os outliers
    - valores mais frequentes
