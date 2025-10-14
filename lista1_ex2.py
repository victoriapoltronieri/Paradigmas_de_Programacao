entrada = input()
contador = 0
entrada_lower = entrada.lower()
vogais = ['a', 'e', 'i', 'o', 'u']
for letra in entrada_lower:
  if letra in vogais:
    contador+=1

print(contador)
