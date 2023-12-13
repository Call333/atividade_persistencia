
'''
r -> read => ler o arquivo
a -> append => adiciona ao arquivo, mantendo aquilo que já existe.
w -> write => sobescreve os arquivos, apagando aquilo que estava escrito antes.
'''

def escreve_nomes(nomes):
    arquivo = open('aula 29-11-2023\meu_nome.txt', 'a', encoding='utf-8')
    arquivo.write(nomes)
    arquivo.close()

def ler_nomes():
    arquivo = open('aula 29-11-2023\meu_nome.txt', 'r', encoding='utf-8')
    nomes = arquivo.read()
    lista = nomes.split(';')
    
    for n in lista:
        print(n)

def main():
    escreve_nomes("Maracujá;jose;maria;pedro;antonio")
    ler_nomes()

if __name__ == '__main__':
    main()

