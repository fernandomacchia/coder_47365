# Clase Cliente, con nombre, email, edad, teléfono 
# con un método imprimir() y método comprar()

#print("\n*** Menú Principal - Segunda pre entrega ***\n")

from paquete1.modulo2 import *

class Cliente:

    clase_cliente = ""

    print("\nElija el tipo de cliente\n")
    print("P: Cliente presencial ")
    print("W: Cliente Web ")
    print("T: Cliente Telefónico ")
    print("S: Salir del sistema ")

    tipo_cliente = input("\n Elija una opción: ").upper()
    if tipo_cliente == "P":
        clase_cliente = ("CLIENTE PRESENCIAL")
    elif tipo_cliente == "W":
        clase_cliente = ("CLIENTE WEB")
    elif tipo_cliente == "T":
        clase_cliente = ("CLIENTE TELEFÓNICO")
    elif tipo_cliente == "S":
        print("\nUsted salió correctamente del sistema. Gracias")
        #break
    else:
        print("\nElija una opción válida (entre P, W, T o S)")


    def __init__(self, nombre, email, edad, telefono):
        self.nombre = input("Ingrese su nombre: ").upper()
        self.email = input("Ingrese su email: ").upper()
        self.edad = int(input("Ingrese su edad: "))
        self.telefono = int(input("Ingrese su teléfono: "))

    def comprar(self, producto, comercio, precio, metododepago):
        self.producto = input("Ingrese el producto que compró: ").upper()
        self.comercio = input("Ingrese el nombre del comercio: ").upper()
        self.precio = int(input("Ingrese el percio pagado: "))
        self.metododepago = input("Ingrese el método de pago elegido: ").upper()
        print(f'\nEl producto comprado fue un/una {self.producto}. \nLa compra fue hecha en el comercio {self.comercio}. \nEl precio abonado fue ${self.precio}\nEl método de pagó que usó fue {self.metododepago}\n')

    #return self.nombre
    def __str__(self):
        return f'\nBienvenido {self.nombre}, usted es un {self.clase_cliente}\n'

    def imprimir(self):
        print(f'Los datos ingresados por usted son: \nEmail: {self.email} \nEdad: {self.edad} años \nTeléfono: {self.telefono}\n')






