
from datetime import date

# class Extrato:
#     def __init__(self):

class Lancamento:
    def __init__(self, data, valor):
        self.data = data
        self.valor = valor


saldo = float(0)
extrato = [];

def entrada():
    valor = float(input("Digite um valor(ele pode ser positivo ou negativo): R$ "))
    today = date.today()
    lancamento = Lancamento(today, valor)

    global extrato
    extrato.append(lancamento)

    global saldo
    saldo += valor
    print("saldo: R${} ".format(saldo))

def consultar_saldo():
    print(saldo)

def exibir_extrato():
    index = 0
    global extrato
    while ( index < len(extrato)):
        print(
            """
            ---------------
            data: {}
            valor: R$ {:.2f}
            ---------------    
            """
              
              .format(
                  extrato[index].data,
                  extrato[index].valor))
        index += 1
    

def main():
    while(True):
        opcao = int(input("""
                          [1] - Informar entrada ou saida
                          [2] - Consultar saldo
                          [3] - Exibir extrato
                          [99] - Encerrar programa                          
                          """))
        match opcao :
            case 1: 
                entrada()
            case 2:
                consultar_saldo()
            case 3:
                exibir_extrato()
            case _:
                print("valor invalido. Seleione outra coisa.")


if __name__ == "__main__":
    main()