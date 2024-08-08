from rodar import Padrao
import subprocess
import os

class Installer(Padrao):
    
    COMspec: str = os.getenv("COMSPEC")

    def __init__(self, nome: str):
        self.nome = nome

    def rodar(self):
        ## Colocar o powershell como padrão de execução
        os.putenv('COMSPEC',r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')
        
        ## Configuração do PATH 
               
        r = subprocess.run(
            f'[System.Environment]::SetEnvironmentVariable("PATH", "$env:PATH;{os.path.join(os.path.expanduser("~"), "nodejs", self.nome)}", [System.EnvironmentVariableTarget]::User)', 
            shell=True,
            capture_output=True)
        print(r.stdout)

        ## Instalação do Angular
        r = subprocess.run(
            'npm install -g @angular/cli', 
            shell=True,
            capture_output=True)
        print(r.stdout)

        ## Criação de um projeto
        r = subprocess.run(
            'ng.cmd new --style "css" --skip-git padrao', 
            shell=True,
            capture_output=True)
        print(r.stdout)

        ## Restauração de COMSPEC
        os.putenv(self.COMspec)

