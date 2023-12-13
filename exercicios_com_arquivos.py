'''
Feito Por Calebe A. Melo a
'''

dadosUsers = []

def escreve_nomes(dados):
    arquivo = open('aula 29-11-2023\dados_dos_usuarios.txt', 'a', encoding='utf-8')
    arquivo.write(dados+"\n")
    arquivo.close()

def ler_nomes():
    arquivo = open('aula 29-11-2023\dados_dos_usuarios.txt', 'r', encoding='utf-8')
    nomes = arquivo.read()
    listaDeUsers = nomes.split("\n")
    print(listaDeUsers)
    for l in listaDeUsers:
        dadosUsers.append(l.split(" | "))
    
    for i in dadosUsers:
        if(i == ['']):
            dadosUsers.remove(i)

    for users in dadosUsers:
        print("**** Usuário ****")
        print(f"Nome: {users[0]}")
        print(f"Idade: {users[1]}")
        if(users[2] == "M"):
            print(f"Sexo: Masculino[{users[2]}]")
        elif(users[2] == "F"):
            print(f"Sexo: Feminino[{users[2]}]")
        else:
            print(f"Sexo: Não informou")
        print(f"Telefone: {users[3]}")
        print("")

def busca_usuario_por_sexo(sexo):
    print("FUNçÃO BUSCA SExO")
    for s in dadosUsers:
        if(s[2] == sexo.upper()):
            print(s)

def busca_usuario_por_nome(nome_procurado):
    print("FUNÇÃO NOME PROCURADO")
    for nome in dadosUsers:
        if(nome_procurado.lower() in nome[0].lower()):
            print(nome)
            

def m0():
    print("Sistema de cadastro de dados")
    while True:
        nome = input("Digite o seu nome: ")
        if(nome == "0"):
            print("Fim do programa...")
            break
        idade = int(input("Digite a sua idade: "))
        sexo = input("Digite M para Masculino ou F para Feminino: ")
        print("Digite o número de telefone Ex: 988887777: ")
        telefone = int(input(""))

        escreve_nomes(f"{nome} | {idade} | {sexo} | {telefone}")
    ler_nomes()
    busca_usuario_por_sexo("")
    busca_usuario_por_nome('c')
    
m0()