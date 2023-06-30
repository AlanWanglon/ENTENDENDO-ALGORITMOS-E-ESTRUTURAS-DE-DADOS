def contar(i):
    if i <= 0:
        return 0
    else:
        print(i)
        return contar(i-1)

contar(9)