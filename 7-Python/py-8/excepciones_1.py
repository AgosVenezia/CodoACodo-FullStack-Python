try:    
    num1= int(input("Ingrese un número:"))
    num2= int(input("Ingrese un número:"))    #ValueError
    resultado= num1/num2                      #ZeroDivisionError
    #resultado= num/num2                       #NameError
    print(resultado)

except ValueError:
    print("Debe ingresar un valor numérico.")
except ZeroDivisionError:
    print("El 2do número no puede ser cero.")
except:
    print("Error!")
else:
    print(resultado)
finally:
    print("Siempre se ejecuta")

print("Fin!")
