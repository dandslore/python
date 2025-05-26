# R$60,00 por dia e R$0,15 por km rodado
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
preço = (60 * dias) + (0.15 * km)
print('O total a pagar é R${:.2f}'.format(preço))
