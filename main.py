from downloader import Downloader
from extrator import Extrator
from versioner import Versioner
from installer import Installer
from type import Type
from gui import Gui

### Um software de automação do Pedro - livre para distribuição e modificação ###

# Declaração de variáveis #
pacote: str
versao: str

tsconfig: str = r"""
{
      "compilerOptions": {
          "target": "ES5",
          "module": "CommonJS",
          "outDir": "js"
      }
}
"""
tasks: str = r"""
  {
      "version": "2.0.0",
      "tasks": [
        {
          "label": "compilar",
          "type": "shell",
          "command": "tsc",
          "args": [
            "-p",
            "tsconfig.json"
          ],
          "group": {
            "kind": "build",
            "isDefault": true
          },
        },
        {
          "label": "rodar",
          "type": "shell",
          "command": "node",
          "args": [
            "js/${fileBasenameNoExtension}.js"
          ],
          "group": {
            "kind": "test",
            "isDefault": true
          },
        }
      ]
  }
"""

## Versao atual #
versao = Versioner("https://nodejs.org/dist/latest").rodar()
pacote = f"node-{versao}-win-x64.zip"

## Funções macro #
def exec_tudo():

  ## Download do pacote && Extração #
  Downloader(f"https://nodejs.org/dist/latest/{pacote}", pacote).rodar()
  Extrator(pacote).rodar()
  Installer(f"node-{versao}-win-x64").rodar()

  ## Configuração do ambiente do TypeScript
  Type(tsconfig,tasks).rodar()

def num_versao():
    print(Versioner("https://nodejs.org/dist/latest").rodar())

## Interface #
Gui(
    {
        "Instalar tudo": exec_tudo,
        "Ambiente TypeScript": Type(tsconfig, tasks).rodar,
        "Número da versão": num_versao,
        "Instalação do .zip do nodejs": Downloader(f"https://nodejs.org/dist/latest/{pacote}", pacote).rodar,
        "Instalação do Angular/TypeScript": Installer(f"node-{versao}-win-x64").rodar
    }
).rodar()
