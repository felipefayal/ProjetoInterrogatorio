# Projeto Interrogatório 🕵️

Este é um simples aplicativo de desktop desenvolvido em Python com uma interface gráfica (GUI) usando a biblioteca Tkinter. O programa simula um interrogatório fazendo cinco perguntas a uma pessoa para determinar sua possível participação em um crime fictício. Com base no número de respostas afirmativas, o programa classifica a pessoa como "Inocente", "Suspeita", "Cúmplice" ou "Assassino".

## Funcionalidades

- **Interface Gráfica Amigável**: Interface limpa e moderna construída com Tkinter e estilizada com o módulo `ttk`.
- **Interrogatório Interativo**: Apresenta uma pergunta de cada vez com botões de "Sim" e "Não".
- **Lógica de Classificação**: Classifica o indivíduo com base em regras pré-definidas.
- **Resultado Instantâneo**: Exibe o resultado final em uma caixa de diálogo ao final do questionário.

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação principal.
- **Tkinter**: Biblioteca padrão do Python para a criação de interfaces gráficas.

## Como Executar

Para executar este projeto em sua máquina local, siga os passos abaixo.

**Pré-requisitos:**

- É necessário ter o **Python 3** instalado. A biblioteca Tkinter geralmente já vem incluída nas instalações padrão do Python.

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/felipefayal/ProjetoInterrogatorio.git](https://github.com/felipefayal/ProjetoInterrogatorio.git)
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd ProjetoInterrogatorio
    ```

3.  **Execute o aplicativo:**
    ```bash
    python app.py
    ```

A janela do interrogatório será aberta e você poderá começar a responder às perguntas.

## Regras de Classificação

A classificação final é baseada no número de respostas "Sim":

- **0 ou 1 resposta "Sim"**: Classificado como **Inocente**.
- **2 respostas "Sim"**: Classificado como **Suspeita**.
- **3 ou 4 respostas "Sim"**: Classificado como **Cúmplice**.
- **5 respostas "Sim"**: Classificado como **Assassino**.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.