# Clase Banco que depende de Cuenta
class Banco:
    def __init__(self, nom):
        self.nombre= nom
        self.clientes= [] # Almacenar los datos de mis cuentas
    
    def agregar_cliente(self, cue):
        self.clientes.append(cue)
    
    def __str__(self):
        texto= ''
        texto+= f'Banco: {self.nombre}\n'
        texto+= 'Listado de clientes del banco:\n'
        for cli in self.clientes:
            texto+= str(cli)+'\n'
        texto+= '\n'

        return texto
