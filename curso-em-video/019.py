# Um professor quer sortear um dos seus alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice

aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")
lista_alunos = [aluno1, aluno2, aluno3, aluno4]

aluno_escolhido = choice(lista_alunos)

print(30 * "-")
print(f"O aluno escolhido é: {aluno_escolhido}")
print(30 * "-")