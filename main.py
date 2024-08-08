from downloader import Downloader
from extrator import Extrator
from versioner import Versioner
from installer import Installer
import os

### Um software de automação do Pedro - livre para distribuição e modificação ###
'''
Objetivo:
Fazer 
'''

# Declaração de variáveis #
pacote: str
usuario: str = os.getlogin()
versao: str

# Interface # 
print(f"Bem-vindo {usuario}!")
if input("Deseja realmente executar este programa? (s/n) $ ").lower() != "s":
    exit()

## Versao atual #
versao = Versioner("https://nodejs.org/dist/latest").rodar()
pacote = f"node-{versao}-win-x64.zip"

## Download do pacote && Extração #
Downloader(f"https://nodejs.org/dist/latest/{pacote}", pacote).rodar()
Extrator(pacote).rodar()

Installer(os.path.join("nodejs", f"node-{versao}-win-x64")).rodar()