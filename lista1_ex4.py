entrada = int(input())
soma = 0
digits= []

digits = [int(digit) for digit in str(entrada)]

for i in range(len(digits)):
  soma = soma + digits[i]
print(soma)
