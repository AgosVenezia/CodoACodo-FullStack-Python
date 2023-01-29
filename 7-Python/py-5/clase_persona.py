# Declarar una clase
class Persona:
    def inicializar(self, n, e):
        self.nombre= n # Atributo
        self.edad= e

    def imprimir(self):
        print("Nombre: " + self.nombre + " Edad: " + str(self.edad))

# Prog Ppal
persona1= Persona() # Instanciando la clase
persona1.inicializar("Ramiro", 40)
persona1.imprimir()

persona2= Persona()
# print(persona1)
# print(persona2)
print(type(persona2))
texto= "Hola Mundo!"
print(type(texto)) # type me devuelve la clase del objeto

# Objeto que contiene un objeto
lista= [1, "Texto", 10.00, True] # Intancia de un objeto de tipo Lista
print(lista[1].upper())
