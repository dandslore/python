lista_hortifruti = []


def leitura_produtos():
    quantidade_n = int(input())

    i = 0
    while i < quantidade_n:
        produto = input()

        # Caso o produto já tenha sido cadastrado, a mensagem “Produto já cadastrado" deve aparecer na tela.
        if produto in lista_hortifruti:
            print("Produto já cadastrado")
        else:
            preco_produto = float(input())

            lista_hortifruti.append(produto)
            lista_hortifruti.append(preco_produto)
            
            i = i+1
    
# seu programa deve em seguida ler o nome de vários hortifrutis e imprimir o seu preço caso o produto esteja na lista lida inicialmente.
def busca_produtos():
    while True:
        busca = input()
        if busca == "Fim": # A busca pelo preço de um produto deve ser feita enquanto o usuário não digitar a palavra “Fim”.
            break
        elif busca not in lista_hortifruti:
            print("Produto não cadastrado") # Caso ele não esteja na lista, seu programa deve imprimir a mensagem “Produto não cadastrado”.
        else:
            indice_preco = lista_hortifruti.index(busca) + 1
            print(lista_hortifruti[indice_preco])


leitura_produtos()
busca_produtos()
