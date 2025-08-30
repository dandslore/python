# Problema prático 3.3 do livro Introdução à computação 
# usando Python: um foco no desenvolvimento de aplicações
# (a) Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; 
# caso contrário, exiba 'Definitivamente não é um ano bissexto.'

ano = int(input("Digite um ano: "))

if ano % 4 == 0:

    print("Pode ser um ano bissexto.")

else:

    print("Definitivamente não é um ano bissexto.")


    # Se um ano for divisível por 100, ele só será bissexto se também for divisível por 400.