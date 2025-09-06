n = int(input('Digite um número para ver sua tabuada: '))

contador = 1
print(10 * '-')
while(contador <= 1000):
    print('{} x {} = {}'.format(contador, n, n * contador))
    contador += 1
print(10 * '-')