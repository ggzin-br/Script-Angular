from rodar import Padrao
import tkinter as tk

class Gui(Padrao):

    def __init__(self, dict_elel: dict):
        self.janela = tk.Tk()
        
        self.chaves = list(dict_elel.keys())
        self.dicionario = dict_elel

    def rodar(self):
    
        self.janela.title = "Script Angular"

        ## Botões
        for chave in self.chaves:
            tk.Button(self.janela, 
                      text=chave, 
                      command=self.dicionario[chave]
                      ).pack(side=tk.TOP, padx=10, pady=10)

        ## Janela
        self.janela.mainloop()