
numero = int(input("Digite um número natural (inteiro e positivo): "))

def somar(numero):
    if numero == 0:
        return 0
    return numero + somar(numero - 1)

print(f"A soma de todos os números até {numero} é: {somar(numero)}")