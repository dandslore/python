# Problema prático 3.4 do livro Introdução à computação 
# usando Python: um foco no desenvolvimento de aplicações

# Implemente um programa que comece pedindo ao usuário para 
# digitar uma identificação de login (ou seja, uma string). 
# O programa, então, verifica se a identificação informada pelo usuário está na lista 
# ['joe', 'sue', 'hani', 'sophie' ] de usuários válidos. 
# Dependendo do resultado, uma mensagem apropriada deverá ser impressa. 
# Não importando o resultado, sua função deverá exibir 'Fim.' antes de terminar. 

lista_usuarios = ['joe', 'sue', 'hani', 'sophie']

usuario = input("Login: ")

if usuario in lista_usuarios:
    
    print("Acesso permitido.")

else:
    print("Acesso negado. \nUsuário desconhecido.")