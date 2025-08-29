# Faça um programa que leia um ângulo qualquer 
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = radians(float(input("Insira um ângulo qualquer: ")))

print("Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}".format(sin(angulo), cos(angulo), tan(angulo)))