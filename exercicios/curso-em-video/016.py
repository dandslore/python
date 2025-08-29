# Crie um programa que leia um número real qualquer pelo teclado 
# e mostre na tela a sua porção inteira.

from math import trunc

print("-" * 5, "Porção inteira de um número real", "-" * 5)
num = float(input("Digite um número real: "))
print("O número digitado foi {}, sua porção inteira é {}.".format(num, trunc(num)))

#opção sem importar biblioteca
#print("O número digitado foi {}, sua porção inteira é {}.".format(num, int(num)))