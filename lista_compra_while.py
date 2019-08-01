

lista_compra = []
input_usuario = ""

while input_usuario != "FIN":
    input_usuario = input("Que necesitas comprar? (escribe FIN para salir): ")
    if input_usuario != "FIN":
        lista_compra.append(input_usuario)

largo_lista = len(lista_compra)
indice_actual = 0

while indice_actual < largo_lista:
    print("Tengo que comprar {}".format(lista_compra[indice_actual]))
    indice_actual += 1

for item in lista_compra:
    print("Tengo que comprar {}".format(item))

print("Es la lista de la compra")