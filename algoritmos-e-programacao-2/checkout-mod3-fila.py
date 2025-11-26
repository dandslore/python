class Fila:
    def __init__(self):
        """Inicializa uma fila vazia"""
        self.itens = []
    
    def enfileirar(self, elemento):
        """Insere um elemento no final da fila"""
        self.itens.append(elemento)
        print(f"Elemento '{elemento}' adicionado à fila.")
    
    def desenfileirar(self):
        """Remove e retorna o elemento do início da fila"""
        if self.esta_vazia():
            print("A fila está vazia! Não é possível remover elementos.")
            return None
        elemento = self.itens.pop(0)
        print(f"Elemento '{elemento}' removido da fila.")
        return elemento
    
    def consultar(self):
        """Exibe o elemento do início da fila sem removê-lo"""
        if self.esta_vazia():
            print("A fila está vazia!")
            return None
        elemento = self.itens[0]
        print(f"Primeiro elemento da fila: '{elemento}'")
        return elemento
    
    def contar(self):
        """Retorna a quantidade de elementos na fila"""
        quantidade = len(self.itens)
        print(f"A fila possui {quantidade} elemento(s).")
        return quantidade
    
    def esta_vazia(self):
        """Verifica se a fila está vazia"""
        return len(self.itens) == 0
    
    def exibir_fila(self):
        """Exibe todos os elementos da fila"""
        if self.esta_vazia():
            print("Fila: []")
        else:
            print(f"Fila: {self.itens}")

def menu():
    """Exibe o menu de opções para o usuário"""
    print("\n" + "="*50)
    print("           OPERAÇÕES COM FILA")
    print("="*50)
    print("1. Enfileirar (adicionar elemento)")
    print("2. Desenfileirar (remover elemento)")
    print("3. Consultar primeiro elemento")
    print("4. Contar elementos")
    print("5. Exibir fila completa")
    print("6. Sair")
    print("="*50)

def main():
    """Função principal do programa"""
    # Cria uma fila vazia
    fila = Fila()
    
    while True:
        menu()
        
        try:
            opcao = input("\nDigite a opção desejada (1-6): ").strip()
            
            if opcao == "1":
                elemento = input("Digite o elemento a ser adicionado: ").strip()
                if elemento:
                    fila.enfileirar(elemento)
                else:
                    print("Erro: Elemento não pode ser vazio!")
            
            elif opcao == "2":
                fila.desenfileirar()
            
            elif opcao == "3":
                fila.consultar()
            
            elif opcao == "4":
                fila.contar()
            
            elif opcao == "5":
                fila.exibir_fila()
            
            elif opcao == "6":
                print("\nPrograma encerrado.")
                break
            
            else:
                print("Opção inválida! Por favor, digite um número entre 1 e 6.")
        
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")

# Executa o programa
if __name__ == "__main__":
    main()