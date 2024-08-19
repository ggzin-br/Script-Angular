# Este programa faz a extração de um .zip passado no construtor (o diretório dele).
# A saída fica no "~"/nodejs.

import zipfile
import os
from rodar import Padrao

class Extrator(Padrao):

    ## Declaração de variáveis #
    path: str = os.path.join(os.path.expanduser("~"), "nodejs")
    zip: str

    def __init__(self, zip: str):
        self.zip = os.path.join(os.path.expanduser("~"), zip)

    def rodar(self):
        
        ## Extração do zip para a pasta "nodejs" no $HOME
        with zipfile.ZipFile(self.zip, "r") as zip:
            try:
                os.mkdir(self.path)
            except FileExistsError:
                print("O diretório já existe, prosseguindo com a instalação...")
            
            zip.extractall(self.path)
