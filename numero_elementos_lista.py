def count(lista):
    if not lista:
        return 0
    return 1 + count(lista[1:])

lista = [0,4,5,6,7]
numero = count(lista)
print(numero)