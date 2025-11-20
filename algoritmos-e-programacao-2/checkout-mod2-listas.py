# Crie um novo script em Python.
# Importe o módulo “random” para poder trabalhar com números aleatórios.
# Crie uma lista para ser preenchida com 100 números inteiros.
# Preencha a lista criada com números gerados aleatoriamente. Dica: use a função “randint()” do módulo “random”.
# Percorra novamente a lista preenchida e separe os números pares em uma lista e os números ímpares em outra.
# Exiba na tela o conteúdo das três listas: a original, a lista de pares e a lista de ímpares.

import random

lista100 = [random.randint(1, 500) for _ in range(100)]
print(f"Lista original: {lista100}")
print(100*"-")

listapares = []
listaimpares = []

for i in lista100:
    if i % 2 == 0:
        listapares.append(i)
    else:
        listaimpares.append(i)

print(f"Lista de pares: {listapares}")
print(100*"-")
print(f"Lista ímpares: {listaimpares}")