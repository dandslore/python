import csv
from datetime import datetime
from pathlib import Path
from typing import List

class Lancamento:
    def __init__(self, data: datetime, valor: float, descricao: str = ""):
        self.data = data
        self.valor = valor
        self.descricao = descricao

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y')}\t{self.formatar_valor()}\t{self.descricao}"

    def formatar_valor(self) -> str:
        return f"R$ {self.valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def to_dict(self) -> dict:
        return {
            'data': self.data.strftime('%Y-%m-%d'),
            'valor': self.valor,
            'descricao': self.descricao
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            datetime.strptime(data['data'], '%Y-%m-%d'),
            float(data['valor']),
            data['descricao']
        )


class Extrato:
    def __init__(self):
        self.lancamentos: List[Lancamento] = []
        self.arquivo_csv = Path("extrato.csv")
        self.carregar_extrato()

    @property
    def saldo(self) -> float:
        return sum(lancamento.valor for lancamento in self.lancamentos)

    def adicionar_lancamento(self, valor: float, descricao: str = ""):
        lancamento = Lancamento(datetime.now(), valor, descricao)
        self.lancamentos.append(lancamento)
        self.salvar_lancamento(lancamento)
        print(f"Lançamento realizado. Saldo atual: {self.formatar_saldo()}")

    def formatar_saldo(self) -> str:
        return f"R$ {self.saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def exibir_extrato(self):
        print("\n" + "=" * 60)
        print("EXTRATO BANCÁRIO".center(60))
        print("=" * 60)
        print("DATA\t\tVALOR\t\tDESCRIÇÃO")
        print("-" * 60)
        
        for lancamento in self.lancamentos:
            print(lancamento)
        
        print("-" * 60)
        print(f"SALDO TOTAL: {self.formatar_saldo()}".rjust(60))
        print("=" * 60 + "\n")

    def salvar_lancamento(self, lancamento: Lancamento):
        file_exists = self.arquivo_csv.exists()
        
        with open(self.arquivo_csv, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['data', 'valor', 'descricao'])
            
            if not file_exists:
                writer.writeheader()
            
            writer.writerow(lancamento.to_dict())

    def carregar_extrato(self):
        if not self.arquivo_csv.exists():
            return
            
        with open(self.arquivo_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.lancamentos.append(Lancamento.from_dict(row))


class BancoApp:
    def __init__(self):
        self.extrato = Extrato()

    def menu_principal(self):
        while True:
            try:
                opcao = input("""
                [1] - Adicionar lançamento (débito ou crédito)
                [2] - Consultar saldo
                [3] - Exibir extrato completo
                [4] - Sair do programa
                
                Escolha uma opção: """).strip()

                match opcao:
                    case '1':
                        self.adicionar_lancamento()
                    case '2':
                        self.consultar_saldo()
                    case '3':
                        self.extrato.exibir_extrato()
                    case '4':
                        print("Encerrando o programa...")
                        break
                    case _:
                        print("Opção inválida. Por favor, escolha uma opção válida.")
            except ValueError as e:
                print(f"Erro: {e}. Por favor, tente novamente.")

    def adicionar_lancamento(self):
        try:
            valor = float(input("Digite o valor (positivo para crédito, negativo para débito): R$ "))
            descricao = input("Descrição (opcional): ").strip()
            self.extrato.adicionar_lancamento(valor, descricao)
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

    def consultar_saldo(self):
        print(f"\nSaldo atual: {self.extrato.formatar_saldo()}\n")


def main():
    app = BancoApp()
    app.menu_principal()


if __name__ == "__main__":
    main()