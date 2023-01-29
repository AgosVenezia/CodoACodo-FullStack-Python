from class_animal import Animal  #mporta todo lo que está en el programa principal, por eso dos veces emite sonido
from class_gato import Gato
from class_perro import Perro

def __main__():
    #a1= Animal()      TypeError: Can't instantiate abstract class Animal with abstract methods
    #a1.emitir_sonido()
    g1= Gato()
    g1.emitir_sonido()
    p1= Perro()
    p1.emitir_sonido()

animales= []
animales.append(g1)
animales.append(p1)

for animal in animales:
    animal.emitir_sonido()

__main__() 
