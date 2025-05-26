real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = float(5.59)
# resultado = float(real / dolar)
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, real / dolar))
