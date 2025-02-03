Gerenciador de Tarefas com Streamlit

Este é um simples gerenciador de tarefas, desenvolvido em Python com Streamlit, onde os usuários podem adicionar, exibir e remover tarefas de uma lista interativa. O projeto usa o estado de sessão do Streamlit para armazenar as tarefas de maneira temporária.

 ## Funcionalidades

- **Adicionar Tarefa**: Permite que o usuário adicione novas tarefas à lista.
- **Exibir Tarefas**: Exibe a lista de todas as tarefas cadastradas.
- **Remover Tarefa**: Permite que o usuário remova tarefas específicas da lista.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Streamlit**: Framework utilizado para criar a interface interativa.
- **Pandas**: Biblioteca utilizada para exibição das tarefas em formato de tabela.

## Como Rodar

### Requisitos

Antes de rodar o código, você precisa ter o Python instalado. Além disso, é necessário instalar as dependências do projeto:

1. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    ```

2. Ative o ambiente virtual:

    - No Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - No Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

3. Instale as dependências:

    ```bash
    pip install streamlit pandas
    ```

### Execução

1. Execute o aplicativo Streamlit:

    ```bash
    streamlit run app.py
    ```

2. Acesse o aplicativo através do navegador em `http://localhost:8501`.

## Personalização

- **Ícones e Imagens**: O app inclui ícones e uma imagem de logo que você pode substituir conforme necessário (certifique-se de ter as imagens `logo.jpg` e `iconesite.png` no diretório do projeto).
- **Estilo**: O código também inclui um arquivo CSS (`style.css`) para personalização da aparência. Certifique-se de ter o arquivo de estilo no diretório correto.

## Como Contribuir

Se você quiser contribuir com melhorias ou correções, siga os passos abaixo:

1. Faça o fork deste repositório.
2. Crie uma branch para sua feature (`git checkout -b feature-nome`).
3. Faça as alterações desejadas e envie um pull request.

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
<p align="center">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
</p>

