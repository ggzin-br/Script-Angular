from rodar import Padrao
import os

class Type(Padrao):


    def __init__(self, tscconfig: str, tasksconfig):
        self.typeenv = os.path.join(os.path.expanduser("~"), "type-env")
        self.tscconfig = tscconfig
        self.tasksconfig = tasksconfig

    def rodar(self):
        
        ## Criar o diretório e os arquivos para o Type
        try:
            os.mkdir(self.typeenv)
            os.mkdir(os.path.join(self.typeenv, ".vscode"))
            os.mkdir(os.path.join(self.typeenv, "js"))
        except FileExistsError as e:
            print(f"O diretório já existe, prosseguindo com a instalação...: \n{e}")
        except FileNotFoundError:
            SystemError(FileNotFoundError)

        with open(os.path.join(self.typeenv, "tsconfig.json"), "+w") as arq: # já da o .close()
            arq.write(self.tscconfig)
        with open(os.path.join(self.typeenv, ".vscode", "tasks.json"), "w+") as arq:
            arq.write(self.tasksconfig)