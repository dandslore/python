# Faça um programa que leia um ângulo qualquer 
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = radians(float(input("Insira um ângulo qualquer: ")))

print(f"Seno: {sin(angulo):.2f} \nCosseno: {cos(angulo):.2f} \nTangente: {tan(angulo):.2f}")