# Esse programa agrega todos os objetos para ser executado pelo onclick no Gui.
# É separado em funções para ser capaz executar comandos unitários ou duplos

import os

class Runner():

    ## Declaração de variáveis #
    objs: dict
    vars: dict

    def __init__(self, objs: dict, vars: dict):
        self.objs = objs
        self.vars = vars
    
    def tudo(self):
        ## Download do pacote && Extração #
        self.objs["Downloader"](self.vars["link"]+"/"+self.vars["zip"], self.vars["zip"]).rodar()
        self.objs["Extrator"](self.vars["zip"]).rodar()
        self.objs["Installer"](self.vars["pacote"]).rodar()
        self.objs["Projeter"](self.vars["pacote"]).rodar()

        ## Configuração do ambiente do TypeScript #
        self.objs["Type"]("type-env", self.vars["tsconfig"], self.vars["tasks"]).rodar()
    

    def path(self):
        print(f'[System.Environment]::SetEnvironmentVariable("PATH", "$env:PATH;{os.path.join(os.path.expanduser("~"), "nodejs", self.vars["pacote"])}", [System.EnvironmentVariableTarget]::User)')

    def download(self):
        self.objs["Downloader"](self.vars["link"]+"/"+self.vars["zip"], self.vars["zip"]).rodar()
        self.objs["Extrator"](self.vars["zip"]).rodar()

    def type(self):
        self.objs["Type"]("type-env", self.vars["tsconfig"], self.vars["tasks"]).rodar()
    
    def ang_e_type_inst(self):
        self.objs["Installer"](self.vars["pacote"]).rodar() 
    
    def prog(self):
        self.objs["Projeter"](self.vars["pacote"]).rodar()