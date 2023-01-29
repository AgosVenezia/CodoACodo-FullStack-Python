# Cuenta: es una clase atómica
class Cuenta:
    # Atributo de clase
    # banco= "Santa" # Debería estar en la clase "Banco"
    def __init__(self, nom):
        # Atributos
        self.__titular= nom # At. de instancia
        self.__saldo= 0

    # Getters (obtener) y Setters (modificar)
    # getter de saldo
    # decoradores
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,  nom):
        if nom!='':
            self.__titular= nom

    @property
    def saldo(self):
        return self.__saldo

    # Métodos de instancia
    def depositar(self, importe):
        if importe>0:
            self.__saldo+= importe
    
    def extraer(self, importe):
        if importe<=self.__saldo:
            self.__saldo-= importe

    # Método especial: str
    def __str__(self):
        return f'Titular: {self.__titular} Saldo actual: ${self.__saldo}.'
    
    def __del__(self):
        # Eliminar los mov. asociados a esa cuenta
        pass # una instruccion que no hace nada

# Probar nuestra clase Cuenta
'''
c1= Cuenta("Ramiro")
c2= Cuenta("Laura")
print(c1)
print(c2)

c1.depositar(1000)
c1.extraer(100)
c2.depositar(2000)

# Verificando el estado del objeto a través del método str
print(c1)
print(c2)

# Encapsulamiento (protección de la información del objeto)
# c1.saldo= 10000 # AttributeError: can't set attribute
                # Algo no deseado, no me queda registra del mov.
                # Algo no deseado, acceder/modificar al atributo
# c1.__titular= 'Ezequiel Ramiro' # Algo deseado, modificar el nombre del titular
print(c1)
# print(c1.__saldo) # AttributeError: 'Cuenta' object has no attribute '__saldo'
print(c1.saldo)
print(c1.titular)

# Verificar el setter para la propiedad titular
c1.titular= 'Ezequiel Ramiro'
print(c1)

'''
