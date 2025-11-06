def head(x):
    return x[0]

def tail(x):
    return x[1:]

def tamanhoLista(l1):
    if (l1 == []):
        return 0
    else:
        return 1 + tamanhoLista(tail(l1))

def pertence(x,lista):
    if (tamanhoLista(lista) == 0):
        return False
    elif (x == head(lista)):
        return True
    else:
        return pertence(x,tail(lista))

print(pertence(1,[4,2,3,1]))

def concatena(l1,l2):
    if (l1 == [] and l2 == []):
        return []
    elif (l1 == []):
        return concatena(l2,[])
    elif pertence(head(l1),tail(l1)) or pertence(head(l1),l2):
        return concatena(tail(l1),l2)
    else:
        return [head(l1)] + concatena(tail(l1),l2)

print(concatena([1,2],[3,4,1]))
