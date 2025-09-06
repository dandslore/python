# Problema prático 3.2 do livro Introdução à computação 
# usando Python: um foco no desenvolvimento de aplicações
# (c) Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.

from random import randint

golpes = 15
defesas = 0

if golpes > 10 and defesas == 0:
    print("Você está morto...")