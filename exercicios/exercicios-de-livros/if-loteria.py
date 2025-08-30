# Problema prático 3.3 do livro Introdução à computação 
# usando Python: um foco no desenvolvimento de aplicações
# (b) Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!';
#  se não, exiba 'Melhor sorte da próxima vez…'.

from random import sample

print(10*'-', "ESCOLHA 6 DEZENAS ENTRE 1 E 60", 10*'-')

dez1 = int(input("Insira sua primeira dezena: "))
dez2 = int(input("Insira sua segunda dezena: "))
dez3 = int(input("Insira sua terceira dezena: "))
dez4 = int(input("Insira sua quarta dezena: "))
dez5 = int(input("Insira sua quinta dezena: "))
dez6 = int(input("Insira sua sexta dezena: "))

lista_bilhete = [dez1, dez2, dez3, dez4, dez5, dez6]
lista_bilhete.sort()

lista_loteria = sample(range(1, 60), 6)
lista_loteria.sort()

print(f"Números escolhidos: {lista_bilhete}")
print(f"Números sorteados: {lista_loteria}")

if lista_bilhete == lista_loteria:

    print("Você ganhou!!!")

else:
    print("Mais sorte da próxima vez...")

#Adicionar verificação para caso o usuario insira algo além de números de 1-60