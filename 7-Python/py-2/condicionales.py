# Condicionales simples/dobles
num1=12
num2=5
if num1>10:
    print("num1 es mayor a 10.")
else:
    print("num1 es menor o igual a 10.")

# Condicionales anidados
# Si un alumno promociona, aprueba o desaprueba
nota= int(input("Ingrese la nota del alumno: "))
if nota>=7:
    print("PROMOCIONA!.")
else:
    if nota<=6 and nota>=4:
        print("APRUEBA!.")
    else:
        if nota<4 and nota>=1:
            print("DESAPRUEBA!.")
        else:
            print("Nota no válida.")

# elif
nota= int(input("Ingrese la nota del alumno: "))
if nota>=7:
    print("PROMOCIONA!.")
elif nota<=6 and nota>=4:        #todos los elif alineados al primer if
    print("APRUEBA!.")
elif nota<4 and nota>=1:
    print("DESAPRUEBA!.")
else:
    print("Nota no válida.")

print("Fin del programa!")