def head(x):
    return x[0]

def tail(x):
    return x[1:]

def belong(elem, lista):
    if not lista:
        return 0
    elif head(lista) == elem:
        return 1
    else:
        return belong(elem, tail(lista))

print(belong(1, [3,1,2,5,2]))
