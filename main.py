from downloader import Downloader
from extrator import Extrator
from versioner import Versioner
from installer import Installer
from type import Type
from projeter import Projeter
from gui import Gui
from runner import Runner

# Um software de automação do Pedro - livre para distribuição e modificação #

# Declaração de variáveis #
pacote: str
versao: str
zip: str
link: str = "https://nodejs.org/dist/latest"
tsconfig: str
tasks: str
## Objetos #
runner: Runner
objs: dict = {
  "Downloader": Downloader,
  "Extrator": Extrator,
  "Installer": Installer,
  "Type": Type,
  "Projeter": Projeter,
  "Gui": Gui
}

# Versao atual #
versao = Versioner(link).rodar()
zip = f"node-{versao}-win-x64.zip"
pacote = f"node-{versao}-win-x64"

## Leitura dos arquivos de config
with open("tasks", "r") as arq:
    tasks = arq.read()
with open("tsconfig", "r") as arq:
    tsconfig = arq.read()

## Classe macro
runner = Runner(objs, {
    "pacote": pacote,
    "link": link,
    "zip": zip,
    "tasks": tasks,
    "tsconfig": tsconfig
})

## Interface #
Gui(
    {
        "Instalar tudo": runner.tudo,
        "Criação do projeto": runner.prog,
        "Ambiente TypeScript": runner.type,
        "Instalação do Angular/TypeScript": runner.ang_e_type_inst,
        "Instalação do nodejs": runner.download,
        "PATH": runner.path
    }
).rodar()
