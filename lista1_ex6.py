max = 0
min = 0
for i in range(10):
  entrada = int(input("Digite um número: "))
  if(i == 0):
    max = entrada
    min = entrada
  elif(entrada > max):
    max = entrada
  elif(entrada < min):
     min = entrada

print("O maior número é: ", max)
print("O menor número é: ", min)
