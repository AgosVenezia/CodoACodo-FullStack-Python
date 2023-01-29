#class abstracta
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass 

    @abstractmethod
    def emitir_sonido(self):
        print("Animal emite sonido...", end="")

def __main__():
    a1= Animal ()
    a1.emitir_sonido()

if __name__=="__main__":
    __main__()
    print(__name__)
