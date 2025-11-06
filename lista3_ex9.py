def head(x):
    return x[0]

def tail(x):
    return x[1:]

def conta_maiores(lista, n):
    if not lista:
        return 0
    else:
        if head(lista) > n:
            return 1 + conta_maiores(tail(lista), n)
        else:
            return conta_maiores(tail(lista), n)
numeros = [2, 8, 4, 10, 3]
print(conta_maiores(numeros, 2))
