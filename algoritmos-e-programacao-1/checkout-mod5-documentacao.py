lista_hortifruti = [] # Lista onde serão armazenados os produtos cadastrados


def leitura_produtos():# Função que lê a quantidade de produtos a ser cadastrado em seguida o nome, depois o preço do produto e os armazena em lista_hortifruti
    quantidade_n = int(input()) #Lê a quantidade de produtos a serem cadastrados

    i = 0 # inicia a variavel i para contar as interações do while
    while i < quantidade_n: # i é a variavel contadora e quantidade_n é a quantidade de intens a serem cadastrados informados pelo usuario
        produto = input() # solicita ao usuario o nome do produto a ser cadastrado

        # Condição para verificar se o produto já foi cadastrado
        if produto in lista_hortifruti: # verifica se o produto já está na lista
            print("Produto já cadastrado")
        else:
            preco_produto = float(input()) # Solicita ao usuario o preço do produto a ser cadastrado

            lista_hortifruti.append(produto) # Adiciona o produto na lista_hortifruti
            lista_hortifruti.append(preco_produto) # Adiciona o preço do produto na lista_hortifruti
            
            i = i+1 # Adiciona +1 ao contador 
    

def busca_produtos(): # Lê o nome de vários hortifrutis e imprime o seu preço caso o produto esteja na lista lida inicialmente.
    while True: 
        busca = input() # solicita ao usuario o nome do produto que deseja consultar
        if busca == "Fim": # Encerra a busca de produtos quando o usuário digita "Fim"
            break
        elif busca not in lista_hortifruti:
            print("Produto não cadastrado") # Caso o produto não esteja na lista, imprime a mensagem “Produto não cadastrado”.
        else:
            indice_preco = lista_hortifruti.index(busca) + 1 # localiza o preço do produto na lista, na frente do nome do produto
            print(lista_hortifruti[indice_preco]) # Retorna o nome e valor do produto cadastrado


leitura_produtos() # Chama a função leitura_produtos
busca_produtos() # Chama a função busca_produtos
