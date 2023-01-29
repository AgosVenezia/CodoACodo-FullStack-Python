class Empleado:
    empresa= "Coca Cola" # Atributo de clase

    # Método especial: método constructor
    def __init__(self):
        self.nombre= input("Ingrese un nombre: ")
        self.sueldo= float(input("Ingrese su sueldo: "))
    
    # Método especial: str
    def __str__(self):
        return f'Nombre: {self.nombre}, Sueldo: ${self.sueldo}'
    
    def paga_impuesto(self):
        if self.sueldo>100000:
            paga= True
        else:
            paga= False
        return paga

# Prog Ppal
emp1= Empleado()
print(emp1)
print(emp1.sueldo) # Mostrar una propiedad/atributo
print(emp1.paga_impuesto()) # Invocar/llamar un método

emp2= Empleado()
print(emp1.empresa)
print(emp2.empresa)
print(emp2.sueldo) # Mostrar una propiedad/atributo
Empleado.empresa= "MAC" # Modifico el atributo de clase de Empleado
print(emp1.empresa)
print(emp2.empresa)
