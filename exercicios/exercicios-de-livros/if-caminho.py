# Problema prático 3.2 do livro Introdução à computação
#usando Python: um foco no desenvolvimento de aplicações
#
# (d) Se pelo menos uma das variáveis booleanas 
# norte, sul, leste e oeste for True,
# exiba 'Posso escapar.'.

from random import choice

lista = [True, False]

norte = choice(lista)
sul = False
leste = False
oeste = False

if norte or sul or leste or oeste:
    print('Posso escapar.')