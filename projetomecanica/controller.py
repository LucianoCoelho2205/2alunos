def salvar(nome): #criando a função para salvar o nome
    with open('pessoas.txt', 'a') as arquivo: #abrindo o arquivo pessoas 
        arquivo.write(f"{nome}\n") #

def listar(): #criando função de listar os nomes
    with open('pessoas.txt', 'r') as arquivo: #lendo dados do arquivo função read
        print(arquivo.read())

def listarpessoa(clientefind):
    index = 0
    flag = 0
    arquivo = open("pessoas.txt", "r")

    for line in arquivo:
        index += 1

        if clientefind == eval(line)["nome"]:
            print(line)
            flag = 1
    
    if flag == 0:
        print("nao encontrado")

def deletarpessoa(clientefind):
    index = 0
    flag = 0
    arquivo = open("pessoas.txt", "r")

    for line in arquivo:
        index += 1

        if clientefind == eval(line)["nome"]:
            chave = index
            flag = 1

    arquivo.close()
    
    if flag == 0:
        print("nao encontrado")
    else: 

        try:

            with open("pessoas.txt", "r") as arquivo:

                lines = arquivo.readlines()

                posicao = 1

                with open("pessoas.txt", "w") as arquivo:

                    for line in lines:

                        if posicao != chave:
                            arquivo.write(line)
                        posicao += 1

            print("Pessoa Deletada")

        except:

            print("Erro no processo do Sistema")

