salário = float(input('Qual é o salário do funcionário? R$ '))
aumento = salário + (15 / 100 * salário)
print('Um funcionário que ganhava {:.2f}, com 15% de aumento, passa a receber {:.2f}'.format(salário, aumento))
