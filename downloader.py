import requests
import os
from rodar import Padrao

class Downloader(Padrao):
    def __init__(self, url: str, nome: str):
        self.url = url
        self.nome = nome

    def rodar(self):

        ## Conexão com o servidor #
        try:
            r = requests.get(self.url, allow_redirects=True)
        except requests.exceptions.RequestException as req:
            raise SystemExit(req)
        
        ## Salvamento do arquivo na memória #
        caminho = os.path.join(os.path.expanduser("~"), self.nome)
        with open(caminho, "wb") as arq:
            arq.write(r.content)