'''
28. PY 4 - Funciones
○ Funciones.
○ Concepto.
○ Llamada a función.
○ Retorno y envío de valores.
○ Parámetros, argumentos, valor y referencia.
○ Parámetros mutables e inmutables.
○ Docstring.
○ Parámetros por defecto
○ Funciones Lambda.
○ f-strings

'''
import random

# Crear/Definir/Declarar una función
def sumar(num1, num2): # recibe 2 parámetros
    # docstrings
    ''' 
    Retorna la suma de los 2 valores recibidos.
    2 param:
    par1: un numero entero.
    par2: otro numero entero.

    '''
    resultado= num1+num2
    num1= 0 # Esto no tiene efecto por fuera de su ámbito
    num2= 0
    return resultado # La fx retorna (devuelve) un valor
                     # return al final porque con el return se sale de la fx

# funciones y listas (objetos mutables)
# Ejemplo de una función que NO retorna un valor
def mostrar_lista(lista):
    for valor in lista:
        print(valor, end=' ')
    print()

def sumar_lista(lista):
    ''' Devuelve la sumatoria de los valores de la lista.
    '''
    suma= 0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma

def sumar_contar_lista(lista):
    ''' Devuelve la sumatoria de los valores de la lista.
    '''
    return sum(lista), len(lista) # Retorno 2 valores

def duplicar_valor(num):
    num*= 2
    return num

def duplicar_valores(lista):
    for i in range(len(lista)):
        # lista[i]= lista[i]*2
        lista[i]*= 2

# Prog ppal
# Utilizamos/Invocamos/Llamamos una función
num1= 10
num2= 5
print(sumar(num1, num2)) # recibe 2 argumentos
# help(sumar)
# help(tuple)

# Ámbito de las variables
print('Valor de num1:', num1) # 10

# Llamo a mostrar_lista
lista= [1,2,10,56,80,0,-3]
mostrar_lista(lista)
print('La sumatoria es:', sumar_lista(lista))
# Parámetros mutables e inmutables
duplicar_valores(lista)
mostrar_lista(lista)

# f-strings
# print('Valor num1:', num1)
print(f'Valor num1: {num1}')
print(f'2/3 es {2/3}')
print(f'2/3 es {2/3:.5f}')
print(f'-2/3 es {-2/3:0=12.5f}')

duplicar_valor(num1)
print('Valor num1:', num1)
print('Valor de retorno de la fx:', duplicar_valor(num1))

print()

print(sumar_contar_lista(lista))

# funciones lambda
# Ejemplo: determinar si un número es par o impar.
def es_par(num):
    ''' Devuelve True si el número es par. 
    '''
    if num%2==0:
        rta= True
    else:
        rta= False
    return rta # True/False

def es_par_v2(num):
    ''' Devuelve True si el número es par. 
    '''
    return num%2==0

# Función lambda
es_par_v3= lambda num:num%2==0

print(es_par_v3(2))

# Parámetros por defecto
def raiz(num, r=2):
    return num**(1/r)

print(raiz(4))
print(raiz(125,3)) # 5

# Definir el tipo de dato de un parámetro
# Ejemplo: crear una fx que me devuelva una lista con N elementos.
def crear_lista(N:int):
    '''
    pre: recibe N.
    pos: devuelve una lista creada.
    '''
    lista= []
    for i in range(N):
        lista.append(random.randint(1,100)) # importar la librería
    return lista

lista= crear_lista(10)
palabras= ["RAMIRO", "JUAN", "LAURA"]
mostrar_lista(lista)
mostrar_lista(palabras)

# Parámetros mutables e inmutables (strings)
def reemplazar_en_palabra(palabra:str, texto, nuevo_texto):
    palabra= palabra.replace(texto, nuevo_texto)
    return palabra

palabra= "Hola Mundo!"
print(palabra)
print(reemplazar_en_palabra(palabra, "Mundo", "MUNDO")) # El string es parámetro NO mutable
print(palabra)
