# Clase Cliente, con nombre, email, edad, teléfono 
# con un método imprimir() y método comprar()

print("\n*** Menú Principal - Segunda pre entrega ***\n")

class Cliente:

    def __init__(self, nombre, email, edad, telefono):
        self.nombre = input("Ingrese su nombre: ").upper()
        self.email = input("Ingrese su email: ").lower()
        self.edad = int(input("Ingrese su edad: "))
        self.telefono = int(input("Ingrese su teléfono: "))

    def comprar(self, producto, comercio, precio, metododepago):
        self.producto = input("Ingrese el producto que compró: ")
        self.comercio = input("Ingrese el nombre del comercio: ")
        self.precio = int(input("Ingrese el percio pagado: "))
        self.metododepago = input("Ingrese el método de pago elegido: ")
        print(f'El producto comprado fue un/una {self.producto}. La compra fue hecha en el comercio {self.comercio}. El precio abonado fue ${self.precio} y el método de pagó que usó fue {self.metododepago}')

    #return self.nombre
    def __str__(self):
        return f'Bienvenido {self.nombre}'

    def imprimir(self):
        print(f'Los datos ingresados por usted son: Email: {self.email}, Edad: {self.edad}, Teléfono: {self.telefono}')






