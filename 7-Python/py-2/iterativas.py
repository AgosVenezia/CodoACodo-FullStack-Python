# Iteraciones/Repeticiones (while, for)
# ciclo exacto
# Ejemplo: contador de 1 a 10 (N)

i= 0
N= int(input("Ingrese el valor máximo del contador: "))
while i<N:
    i= i+1
    #break;
    print(i)

# break, continue

#for
for i in range(10):     #0..9
    print(i+1)
for i in range (1,10):  #0..9
    print(i)
for i in range (1,11):  #0..10
    print(i)
for _ in range (1,4,1):
    print("Hola!")
    #print(i)

# Validación
nota= float(input("Ingrese la nota del alumno: "))
#while nota>10 or nota<1:
    #print("Error! La nota debe ser entre 1 y 10.")
    #nota= int(input("Ingrese la nota del alumno: "))

if nota>=7:
    print("PROMOCIONA!.")
elif nota<7 and nota>=4:        #todos los elif alineados al primer if
    print("APRUEBA!.")
else:
    print("DESAPRUEBA!.")