def head(x):
    return x[0]

def tail(x):
    return x[1:]

def is_vogal(c):
    return c.lower() in ['a', 'e', 'i', 'o', 'u']

def ordSublist(lista1, lista2):
    if not lista1 and lista2:  # acabou a lista1 mas ainda faltam consoantes
        return False
    if not lista2:             # já percorremos todas as consoantes da lista2
        return True

    c1 = head(lista1)
    c2 = head(lista2)

    # ignora vogais da lista2
    if is_vogal(c2):
        return ordSublist(lista1, tail(lista2))

    # se as letras forem iguais, avança nas duas
    if c1 == c2:
        return ordSublist(tail(lista1), tail(lista2))
    else:
        # tenta achar o c2 mais à frente na lista1
        return ordSublist(tail(lista1), lista2)
