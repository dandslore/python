# Faça um programa que leia o comprimento do cateto oposto 
# e do cateto adjacente de um truâgulo retâmgulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot, sqrt

cateto_adj = float(input("Digite o valor do cateto adjacente de um triângulo retângulo: "))
cateto_op = float(input("Agora, digite o valor do cateto oposto desse triângulo retângulo: "))
hipotenusa = hypot(cateto_adj, cateto_op)

print("O comprimento da hipotenusa desse triângulo retângulo é: {:.2f}".format(hipotenusa))