from rodar import Padrao
import subprocess
import os

class Installer(Padrao):

    def __init__(self, nome: str, pacote: str):
        self.nome = nome
        self.pacote = pacote

    def rodar(self):
        
        ## Configuração do PATH 
        os.environ["PATH"] += os.pathsep + os.path.join(os.path.expanduser("~"), "nodejs", self.nome)
        dir_install = os.path.join(os.path.expanduser("~"), "nodejs", self.pacote)
        # Este PATH não é definitivo, somente é usado durante a execução do programa

        ## Instalação do Angular
        subprocess.run(
            f'{os.path.join(dir_install, "npm")} install -g @angular/cli', 
            shell=True)
        
        ## Instalação do Tsc
        subprocess.run(
            f'{os.path.join(dir_install, "npm")} install -g typescript --save-dev',
            shell=True)

        ## Criação de um projeto
        subprocess.run(
            f'{os.path.join(dir_install, "ng.cmd")} new --style "css" --skip-git --defaults padrao', 
            shell=True)
        
# Caso precise:
# [System.Environment]::SetEnvironmentVariable("PATH", "$env:PATH;dir", [System.EnvironmentVariableTarget]::User)