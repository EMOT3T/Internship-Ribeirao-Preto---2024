frase = input("Digite uma frase: ")

letras = []

for letra in frase:
    letras.append(letra)

for i in range(len(letras)-1, -1, -1):
    print(letras[i], end='')

frase_invertida = ''.join(letras[::-1])
print("\nFrase invertida:", frase_invertida)


# Recebe a frase do usuário
# Cria uma lista vazia para armazenar as letras da frase
# Percorre a frase e salva cada letra na lista 'letras'
# Imprime as letras na ordem inversa