def func(n):
  return n*10

def map_clone(func, sequencia):
  """
  Função geradora clone do map
  Args:
  - func: Função que será aplicada a cada elemento da seq.
  - sequencia: Iterável a ser consumido pela função
  """

  for el in sequencia:
    yield func(el) # gera o valor apenas quando for pedido (com a chamada next)

iteravel = map_clone(func, [1, 2, 3, 4, 5])

////////////

# Todos os numeros do range ao quadrado
quadrados = [x*x for x in range(5)]
quadrados


////////////
def conta(acc, n):
  return acc[1], acc[0]+acc[1]

def fib(n):
    return functools.reduce(conta, range(0, n), (0, 1))[1]

fib(5)

////////

def concat_reduce(l1, l2):
  return functools.reduce(lambda acc, el: acc + [el], l2, l1)

concat_reduce([1,2,3], [4,5,6])

//////////

# essa ta uma bosta
def concat_map(l1, l2):
  return list(map(lambda a, b: [a]+[b], l1, l2))

print(concat_map([1,2], [3,4]))

/////////

def pertence(lista, x):
  return functools.reduce(lambda acc, el: acc or el==x, lista, False)

pertence([1,2,3], 3)

//////////////
# Dada uma lista de números, calcule a soma dos quadrados apenas dos números pares. (Isso combina map, filter e reduce).

lista = [1, 2, 3, 4, 5, 6] # 1, 4, 9, 16, 25, 36
functools.reduce(lambda a, b: a+b, filter(lambda x: x%2==0, map(lambda x: x**2, lista)))
