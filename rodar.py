from abc import ABC, abstractmethod

class Padrao(ABC):

    @abstractmethod
    def rodar(self):
        pass # Esse pass é bem inútil