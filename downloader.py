# Este programa é responsável por fazer um download a partir de uma URL e salvar no "~".
# Obs: Previamente é usado a classe Versioner para garantir o exec mais novo.

import requests
import os
from rodar import Padrao

class Downloader(Padrao):

    ## Declaração de variáveis #
    url: str
    zip: str

    def __init__(self, url: str, zip: str):
        self.url = url
        self.zip = zip

    def rodar(self):

        ## Conexão com o servidor #
        try:
            r = requests.get(self.url, allow_redirects=True)
        except requests.exceptions.RequestException as req:
            raise SystemExit(req)
        
        ## Salvamento do arquivo na memória #
        caminho = os.path.join(os.path.expanduser("~"), self.zip)
        with open(caminho, "wb") as arq:
            arq.write(r.content)
