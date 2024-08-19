# Esse programa utiliza a biblioteca subprocess que executa comandos de terminal.
# Todo comando é forçado a ser executado no diretório certo do node.
# É praticamente uma classe de instalar pacotes npm.

from rodar import Padrao
import subprocess
import os

class Installer(Padrao):

    ## Declaração de variáveis #
    dir_install: str
    pacote: str

    def __init__(self, pacote: str):
        self.pacote = pacote
        self.dir_install = os.path.join(os.path.expanduser("~"), "nodejs", pacote)

    def rodar(self):
        
        ## Configuração do PATH # 
        os.environ["PATH"] += os.pathsep + os.path.join(os.path.expanduser("~"), "nodejs", self.pacote)
        # Este PATH não é definitivo, somente é usado durante a execução do programa

        ## Instalação do Angular #
        subprocess.run(
            f'{os.path.join(self.dir_install, "npm")} install -g @angular/cli', 
            shell=True)
        
        ## Instalação do Tsc #
        subprocess.run(
            f'{os.path.join(self.dir_install, "npm")} install -g typescript --save-dev',
            shell=True)
        
# Caso precise:
# [System.Environment]::SetEnvironmentVariable("PATH", "$env:PATH;dir", [System.EnvironmentVariableTarget]::User)