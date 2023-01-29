class A:
    def a(self):
        print("Este método lo heredo de A.")

    def b(self):
        print("Este método lo heredo de A.")

class B:
    def b(self):
        print("Este método lo heredo de B.")

class C(B,A):
    def __init__(self):
        print("Soy de la clase C.")
    
    def c(self):
        print("Este método es de C.")

# Prog ppal
a1= A()
a1.a()
a1.b()

b1= B()
b1.b()

c1= C()
c1.c()
c1.a()
c1.b() # Toma el método b de B (ojo con el orden!)
