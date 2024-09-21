from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
import logging

# Configurações do SharePoint
url = " "
login = " "
senha = " "
caminho_arquivo = r" "
pasta_sharepoint = "/sites/seu site/Documentos Compartilhados/pastas"
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class sharepoint:

    def carregar_arquivo(self):
        logging.info('> Vamos carregar o arquivo no sharepoint.')
        # Autenticação usando credenciais de usuário
        credentials = UserCredential(login, senha)
        ctx = ClientContext(url).with_credentials(credentials)

        # Upload do arquivo
        with open(caminho_arquivo, 'rb') as file:
            file_name = caminho_arquivo.split('/')[-1]
            folder = ctx.web.get_folder_by_server_relative_url(pasta_sharepoint)
            folder.upload_file(file_name, file.read()).execute_query()

        logging.info('> Arquivo carregado com sucesso!')


def main():

    start = sharepoint()
    start.carregar_arquivo()

if __name__ == '__main__':
    main()
