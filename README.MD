# Z3R0 ACTIVATOR

## Descrição

O Z3R0 Activator é uma ferramenta que simula um servidor KMS (Key Management Service) para ativar produtos Windows e Office. Ele utiliza o Flask para criar um servidor web que responde a solicitações de ativação e executa comandos específicos para ativar ou remover licenças do Windows e Office.

## Funcionalidades

- **Ativar Windows**: Conecta-se ao servidor KMS e ativa o Windows.
- **Ativar Office**: Conecta-se ao servidor KMS e ativa o Microsoft Office.
- **Ativar Ambos**: Ativa tanto o Windows quanto o Microsoft Office.
- **Remover Licença Atual do Windows**: Remove a licença atual do Windows.

## Requisitos

- Python 3.x
- Flask
- Sistema operacional Windows

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/LastHasagi/activation.git
    cd activation
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Execute o script [kms_activator.py](http://_vscodecontentref_/1):
    ```sh
    python kms_activator.py
    ```

2. O servidor KMS será iniciado e você verá o seguinte menu:
    ```
    [MENU] Escolha uma opção:
    1️⃣ - Ativar Windows
    2️⃣ - Ativar Office
    3️⃣ - Ativar Ambos
    4️⃣ - Remover Licença Atual do Windows

    Digite sua escolha (1, 2, 3 ou 4):
    ```

3. Digite a opção desejada e pressione Enter.

## Estrutura do Projeto


- **kms_activator.py**: Script principal que contém a lógica do servidor KMS e as funções de ativação.
- **requirements.txt**: Arquivo de dependências do Python.
- **.gitignore**: Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo Git.
- **README.md**: Este arquivo de documentação.