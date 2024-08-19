# Esse programa usa a mesma lógica do Installer para executar comandos.
# Essa é uma classe inteiramente para instalação do projeto do Angular.

import os
import subprocess
from rodar import Padrao

class Projeter(Padrao):

    ## Declaração de variáveis #
    dir_install: str

    def __init__(self, pacote: str):
        self.dir_install = os.path.join(os.path.expanduser("~"), "nodejs", pacote)

    def rodar(self):
        
        ## Criação de um projeto #
        subprocess.run(
            f'{os.path.join(self.dir_install, "ng.cmd")} new --style "css" --skip-git --defaults padrao', 
            shell=True)