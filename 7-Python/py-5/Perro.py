# Definiendo mi clase
class Perro:
    # Atributo de clase
    genero= 'Canis'

    # Inicializar un objeto
    # def inicializar(self, nombre):
    #     Atributos de la clase Perro
    #     self.nombre= nombre
    # Métodos especiales (Python)
    # Método especial: init (método constructor)
    def __init__(self, nombre, edad):
        # Atributos de instancia
        self.nombre= nombre
        self.edad= edad

    # Comportamiento (Métodos)
    def ladrar(self):
        return f'{self.nombre} dice guau guau.'

    # def imprimir(self):
    #     return f'{self.nombre} tiene {self.edad} años.'

    # Método especial: str
    def __str__(self):
        return f'{self.nombre} tiene {self.edad} años y su género es {self.genero}.'

# Prog ppal
'''
perro1= Perro('Gordon', '12') # Creando el objeto de tipo perro/instanciando
# perro1.inicializar("Gordon")
print(perro1.ladrar()) # Mensaje a través de un método
# print(perro1.imprimir())
print(perro1) # <__main__.Perro object at 0x0000018AF4DA3FD0>

print(type(perro1)) # <class '__main__.Perro'>

# Ingreso los datos por teclado

nombre= input("Ingrese el nombre del nuevo perro:")
edad= int(input("Ingrese la edad del perro:"))
perro2= Perro(nombre, edad)
print(perro2)
'''
def mostrar_lista(lista):
    print("Elementos de la lista:")
    for valor in lista:
        print(valor)

# Ejemplo: sistema para una vete. 
clientes= [] # lista (objeto) de clientes (perros)
nombre= input("Ingrese el nombre del nuevo perro:")
while (nombre!=''):
    edad= int(input("Ingrese la edad del perro:"))
    perro= Perro(nombre, edad)
    clientes.append(perro)
    nombre= input("Ingrese el nombre del nuevo perro:")

# print(clientes)
mostrar_lista(clientes)
print()

# Modificar el atributo de clase 'genero'
Perro.genero= 'Perro'
mostrar_lista(clientes)
print()

# Mostrando la propiedad de un objeto de mi lista
if len(clientes)>0:
    print(clientes[0].nombre)

# Ejemplo (tarea): mostrar los perros cuya edad supere los 10 años.
# Solución 1: recorro la lista y uso un if
# Solución 2: filter (método)
