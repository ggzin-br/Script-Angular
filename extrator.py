import zipfile
import os
from rodar import Padrao

class Extrator(Padrao):
    def __init__(self, nome: str):
        self.path = os.path.join(os.path.expanduser("~"), "nodejs")
        self.nome = os.path.join(os.path.expanduser("~"), nome)

    def rodar(self):
        
        ## Extração do zip para a pasta "nodejs" no $HOME
        with zipfile.ZipFile(self.nome, "r") as zip:
            try:
                os.mkdir(self.path)
            except FileExistsError:
                print("O diretório já existe, prosseguindo com a instalação...")
            
            zip.extractall(self.path)