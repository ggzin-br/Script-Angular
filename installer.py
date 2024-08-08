from rodar import Padrao
import subprocess
import os

class Installer(Padrao):
    
    com: str

    def __init__(self, nome: str):
        self.nome = nome
    
    def __call__(self):
        r = subprocess.run(self.com, capture_output=True)
        print(r.stdout)

    def rodar(self):
        ## Configuração do PATH
        self.com = ["powershell",
               "-Command", 
               f'[System.Environment]::SetEnvironmentVariable("PATH", "$env:PATH;{os.path.join(os.path.expanduser("~"), self.nome)}", [System.EnvironmentVariableTarget]::User)']
        self.__call__()

        ## Instalação do Angular
        self.com = ["powershell",
                    "-Command",
                    f'npm install -g @angular/cli']
        self.__call__()

        ## Criação de um projeto
        self.com = ["powershell",
                    "-Command",
                    f'ng.cmd new --style "css" --skip-git padrao']
        self.__call__()

