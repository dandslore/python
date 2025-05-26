#lista = [2, 3, 6, 2, 32, 43, 34, 6, 5, 7, 8, 8, 87, 78, 8]
lista = [87, 78, 43, 34, 32, 8, 7, 6, 5, 4, 3, 2, 1, 0,12,123,354,3453,343453,54,5,4,65657676,878797867,6]


quadrado15 = 15**2
contagem_comparacoes = 0
i = 0
while(i < len(lista)):
    j = 0
    while(j < len(lista)):
        if(lista[i] < lista[j]):
            contagem_comparacoes += 1
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
        j += 1
    i += 1
print(lista)
print(quadrado15)
print(contagem_comparacoes)
print(contagem_comparacoes == quadrado15)

matriz = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

matriz[1][3]