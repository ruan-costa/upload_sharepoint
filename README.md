# Upload de Arquivos para SharePoint Utilizando Office365

[![Licença: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

Bem-vindo ao projeto de conexão e upload de arquivos no Microsoft SharePoint! Este projeto utiliza a biblioteca `Office365` para conectar-se ao SharePoint e realizar o carregamento de arquivos.

## 🚀 Funcionalidades
- **Conexão ao SharePoint**: Estabelece conexão com o Microsoft SharePoint utilizando credenciais de login e senha.
- **Upload de Arquivos**: Permite o upload de arquivos para pastas específicas dentro de um site SharePoint.
- **Gerenciamento de Pastas**: Suporte para especificação de caminhos e URLs de diretórios no SharePoint.

## 🛠️ Instalação

### Pré-requisitos
- Python 3.10+
- Conta de acesso ao SharePoint com permissões adequadas
- URL do SharePoint e caminhos das pastas destino

### Instalar Dependências
Na pasta do projeto, execute o comando abaixo para instalar as dependências:
```bash
pip install -r requirements.txt

📋 Uso
1. Configurações Iniciais
Para usar este projeto, você precisará fornecer as seguintes informações:

Login e senha: Credenciais de acesso ao SharePoint.
URL: A URL do site SharePoint onde os arquivos serão carregados.
Caminho das Pastas: O caminho das pastas dentro do SharePoint onde deseja armazenar os arquivos.

from office365.sharepoint.client_context import ClientContext

# Configurações de acesso
url = "https://seu_site_sharepoint.com"
username = "seu_login"
password = "sua_senha"
local_file_path = "caminho/do/arquivo/local"
target_folder_url = "/sites/seu_site/documentos/"

# Conectando e fazendo upload
ctx = ClientContext(url).with_credentials(username, password)
with open(local_file_path, 'rb') as file_content:
    target_folder = ctx.web.get_folder_by_server_relative_url(target_folder_url)
    target_folder.upload_file(file_name, file_content).execute_query()

print("Upload realizado com sucesso!")

📁 Estrutura de Arquivos

.
├── sharepoint_uploader.py      # Script principal para conexão e upload no SharePoint
├── requirements.txt            # Arquivo com as dependências do projeto
├── README.md                   # Este arquivo README


📧 Contato
Se você tiver alguma dúvida, sinta-se à vontade para entrar em contato:

Telefone: (81) 98761-4812
Este projeto simplifica a interação com o SharePoint, facilitando o upload de arquivos diretamente a partir de um script Python! 🎉🚀


Esse `README.md` segue o formato solicitado, descrevendo a função do projeto, os requisitos e exemplos de uso, além de incluir informações de contato.
