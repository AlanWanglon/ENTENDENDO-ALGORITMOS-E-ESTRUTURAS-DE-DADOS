#encontra elemento em uma lista ordenada por busca binaria
def busca_Binaria(lista, alvo):
    if not lista:
        return -1
    baixo = 0
    alto = len(lista) - 1
    meio = (alto + baixo) // 2
    
    # se for igual retorna o valor
    if lista[meio] == alvo:
        return alvo
    
    
    # se o alvo for menor
    elif lista[meio] > alvo:
        
        return busca_Binaria(lista[:meio], alvo)
    
    # se o alvo for maior
    else:
        return busca_Binaria(lista[meio+1:], alvo)
    
lista = [2,4,5,8,9,12,16,23]
n = 9
busca = busca_Binaria(lista,n)
index = lista.index(n)
if busca == -1:
    print('O elemento não está na lista')
else:
    print(f'O número {n} está na lista no indice {index}')