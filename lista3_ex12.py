def head(x):
    return x[0]

def tail(x):
    return x[1:]
    
def concat(lista1, lista2):
    if not lista1:
        return lista2
    else:
        return [head(lista1)] + concat(tail(lista1), lista2)

def inverte(x):
    if not x:
        return []
    else:
    
        return concat(inverte(tail(xs)), [head(xs)])

def geraPalindromo(palavra):
    lista = list(palavra)          # transforma em lista de caracteres
    invertida = inverte(lista)     # gera a versão invertida
    palindromo = concat(lista, invertida)
    return ''.join(palindromo)     # volta para string
