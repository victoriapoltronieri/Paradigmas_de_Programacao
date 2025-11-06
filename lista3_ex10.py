def head(x):
    return x[0]

def tail(x):
    return x[1:]

def concat(lista1, lista2):
    if not lista1:
        return lista2
    else:
        return [head(lista1)] + concat(tail(lista1), lista2)
def filtra_maiores(lista, n):
    if not lista:
        return []
    else:
        if head(lista) > n:
            # adiciona o elemento na frente do resultado recursivo
            return concat([head(lista)], filtra_maiores(tail(lista), n))
        else:
            # ignora o elemento e segue
            return filtra_maiores(tail(lista), n)
