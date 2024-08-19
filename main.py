from downloader import Downloader
from extrator import Extrator
from versioner import Versioner
from installer import Installer
from type import Type
from gui import Gui
import os

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
dir = f"node-{versao}-win-x64"

## Funções macro #
def exec_tudo():

  ## Download do pacote && Extração #
  Downloader(f"https://nodejs.org/dist/latest/{pacote}", pacote).rodar()
  Extrator(pacote).rodar()
  Installer(dir).rodar()

  ## Configuração do ambiente do TypeScript
  Type("type-env", tsconfig,tasks).rodar()

def path():
    print(f'[System.Environment]::SetEnvironmentVariable("PATH", "$env:PATH;{os.path.join(os.path.expanduser("~"), dir)}", [System.EnvironmentVariableTarget]::User)')

## Interface #
Gui(
    {
        "Instalar tudo": exec_tudo,
        "Instalação do Angular/TypeScript": Installer(f"node-{versao}-win-x64").rodar,
        "Ambiente TypeScript": Type("type-env", tsconfig, tasks).rodar,
        "Instalação do .zip do nodejs": Downloader(f"https://nodejs.org/dist/latest/{pacote}", pacote).rodar,
        "PATH": path
    }
).rodar()
