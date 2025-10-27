'''
- Nessa atividade nós iremos desenvolver um programa que simula um sistema de armazenamento de preços dos itens de hortifrutis de um supermercado. 

- Sendo um pouco mais específico, você irá desenvolver um programa em Python que, inicialmente, lê uma quantidade n de frutas ou verduras a serem precificadas. Lida essa quantidade, seu programa deve ler os n produtos em si, juntamente com o preço de cada um deles e guardá-los em uma lista. 
- Atenção: caso o produto já tenha sido cadastrado, a mensagem “Produto já cadastrado" deve aparecer na tela. Feito cadastro dos produtos, seu programa deve em seguida ler o nome de vários hortifrutis e imprimir o seu preço caso o produto esteja na lista lida inicialmente. Caso ele não esteja na lista, seu programa deve imprimir a mensagem “Produto não cadastrado”.

- Ainda sobre o programa a ser desenvolvido, utilize somente uma lista (vide videoaulas 3 da Unidade 2 do Módulo 2 da disciplina) para armazenar os produtos e seus preços. A busca pelo preço de um produto deve ser feita enquanto o usuário não digitar a palavra “Fim”. Lembre-se que a linguagem Python diferencia letras maiúsculas das minúsculas. 
- Assim, Maçã é diferente de maçã. Finalmente, quanto mais modularizado for o seu programa, melhor. Em outras palavras, tente desenvolver uma função para a leitura inicial dos produtos e seu preço e outra para a busca do preço de um certo produto (vide videoaulas 1 e 2 da Unidade 2 do Módulo 3 da disciplina). 
'''

# Você irá desenvolver um programa em Python que, inicialmente, lê uma quantidade n de frutas ou verduras a serem precificadas. Lida essa quantidade, seu programa deve ler os n produtos em si, juntamente com o preço de cada um deles e guardá-los em uma lista. 

lista_hortifruti = []


def leitura_produtos():
    quantidade_n = int(input("Quantos produtos deseja cadastrar? "))

    i = 0
    while i < quantidade_n:
        produto = input("Nome do produto para cadastrar: ")

        # Caso o produto já tenha sido cadastrado, a mensagem “Produto já cadastrado" deve aparecer na tela.
        if produto in lista_hortifruti:
            print("Produto já cadastrado")
        else:
            preco_produto = float(input("preço do produto: "))

            lista_hortifruti.append(produto)
            lista_hortifruti.append(preco_produto)
            
            i = i+1
    print("CADASTRO CONCLUÍDO!")

# seu programa deve em seguida ler o nome de vários hortifrutis e imprimir o seu preço caso o produto esteja na lista lida inicialmente.
def busca_produtos():
    while True:
        busca = input("Nome do produto que deseja consultar (Digite 'Fim' para encerrar a busca): ")
        if busca == "Fim":
            print("Busca encerrada.") # A busca pelo preço de um produto deve ser feita enquanto o usuário não digitar a palavra “Fim”.
            break
        elif busca not in lista_hortifruti:
            print("Produto não cadastrado") # Caso ele não esteja na lista, seu programa deve imprimir a mensagem “Produto não cadastrado”.
        else:
            indice_preco = lista_hortifruti.index(busca) + 1
            print(lista_hortifruti[indice_preco])


leitura_produtos()
print(lista_hortifruti)
busca_produtos()

#As entradas e saídas do algoritmo devem corresponder exatamente aos valores das variáveis descritas no enunciado, não é necessário a impressão de textos ou pontuações adicionais ao que foi solicitado. Abaixo são apresentados dois exemplos de entradas e saídas esperadas. (RETIRAR TEXTOS AO ENVIAR A TAREFA NO VPL)