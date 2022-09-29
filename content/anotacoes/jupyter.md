---
title: "Jupyter"
date: 2022-09-29T08:36:40-03:00
draft: true
---


- Atalhos:
    
    > **Shift + Enter** para executar a célula selecionada;
    > 
    > 
    > **Ctrl+M** + **B** para criar uma célula nóva abaixo;
    > 
    > **Ctrl+M** + **A** para criar uma célula nóva acima;
    > 
    > **Ctrl+M** + **M** para definir a célula selecionada como tipo Texto;
    > 
    > **Ctrl+M** + **Y** para definir a célula selecionada como tipo Código;
    > 


## Google Colab

- Formulários:
    
    ```python
    #@title Exemplos de Campos {run: "auto"}
    
    texto = 'valor da string' #@param {type:"string"}
    melhor_cidade = 'Araraquara' #@param ["Araraquara", "Londres", "Dublin"]
    data_curso = '2019-09-16' #@param {type:"date"}
    number_slider = 6 #@param {type:"slider", min:0, max:10, step:0.1}
    boolean_checkbox = True #@param {type:"boolean"}
    ```
    
