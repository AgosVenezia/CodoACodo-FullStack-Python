# Hacer referencia a las clases Banco y Cuenta
from class_banco import Banco
from class_cuenta import Cuenta # NameError: name 'Cuenta' is not defined

# Prog Ppal (main)
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
c1= Cuenta("Ramiro")
c2= Cuenta("Laura")
c1.depositar(1000)
c1.extraer(100)
c2.depositar(2000)

banco1= Banco('Santa')
print(banco1)
banco1.agregar_cliente(c1)
banco1.agregar_cliente(c2)
print(banco1)
