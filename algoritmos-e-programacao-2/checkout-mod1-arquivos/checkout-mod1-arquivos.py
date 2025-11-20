# Função para substiruir vogais
def substituir_vogais(texto):
    texto = texto.replace('a', '!')
    texto = texto.replace('e', '@')
    texto = texto.replace('i', '#')
    texto = texto.replace('o', '$')
    texto = texto.replace('u', '%')
    return texto

# Função para processar o arquivo

def processar_arquivo(entrada, saida):
    try:
        with open(entrada, 'r', encoding='utf-8') as arquivo_entrada:
            conteudo = arquivo_entrada.read()

        conteudo_codificado = substituir_vogais(conteudo)

        with open(saida, 'w', encoding='utf-8') as arquivo_saida:
            arquivo_saida.write(conteudo_codificado)

        print(f"Arquivo processado com sucesso! Salvo em {saida}")
        return True

    except FileNotFoundError:
        print(f"Erro: Arquivo '{entrada}' não encontrado.")
        return False
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        return False




arquivo_entrada = "musica.txt"
arquivo_saida = input("Digite o nome do arquivo de saída: ")
processar_arquivo(arquivo_entrada, arquivo_saida)