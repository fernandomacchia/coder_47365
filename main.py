from paquete1.modulo1 import Cliente


#print("\n*** Menú Principal - Segunda pre entrega ***\n")

cliente1 = Cliente("nombre", "email", "edad", "telefono")

# Imprime self
print(cliente1)

# llamo al método imprimir
cliente1.imprimir()

# llamo al método comprar
cliente1.comprar("producto", "comercio", "precio", "metododepago")







