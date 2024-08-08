from rodar import Padrao
import subprocess
import os

class Installer(Padrao):

    def __init__(self, nome: str):
        self.nome = nome

    def rodar(self):
        
        ## Configuração do PATH 
        os.environ["PATH"] += os.pathsep + os.path.join(os.path.expanduser("~"), "nodejs", self.nome)
        # Este PATH não é definitivo, somente é usado durante a execução do programa

        ## Instalação do Angular
        subprocess.run(
            'npm install -g @angular/cli', 
            shell=True)
        
        ## Instalação do Tsc
        subprocess.run(
            'npm install -g typescript --save-dev',
            shell=True)

        ## Criação de um projeto
        subprocess.run(
            'ng.cmd new --style "css" --skip-git --defaults padrao', 
            shell=True)
        
# Caso precise:
# [System.Environment]::SetEnvironmentVariable("PATH", "$env:PATH;dir", [System.EnvironmentVariableTarget]::User)