# Esse programa cria um ambiente do vscode para o typescript.
# Essa classe é inteiramente para a configuração do ambiente.

from rodar import Padrao
import os

class Type(Padrao):

    ## Declaração de variáveis #
    typeenv: str
    tscconfig: str
    tasksconfig: str

    def __init__(self, typeenv: str, tscconfig: str, tasksconfig: str):
        self.typeenv = typeenv
        self.tscconfig = tscconfig
        self.tasksconfig = tasksconfig

    def rodar(self):
        
        ## Criar o diretório e os arquivos para o Type #
        try:
            os.mkdir(self.typeenv) ## Dir do diretório padrão
            os.mkdir(os.path.join(self.typeenv, ".vscode")) 
            os.mkdir(os.path.join(self.typeenv, "js"))
        except FileExistsError:
            print("O diretório já existe, prosseguindo com a instalação...: \n")

        ## Vscode e configs #
        with open(os.path.join(self.typeenv, "tsconfig.json"), "+w") as arq: # já da o .close()
            arq.write(self.tscconfig)
        with open(os.path.join(self.typeenv, ".vscode", "tasks.json"), "w+") as arq:
            arq.write(self.tasksconfig)