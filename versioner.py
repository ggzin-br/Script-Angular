import requests
from rodar import Padrao

class Versioner(Padrao):
    def __init__(self, url: str):
        self.url = url
    
    def rodar(self):
        
        ## Retorno do conteúdo web #
        try:
            r = requests.get(self.url, allow_redirects=True)
        except requests.exceptions.RequestException as req:
            raise SystemExit(req)
    
        conteudo = str(r.content).split("-")
        for versao in conteudo:
            if versao[0] == "v":
                return versao