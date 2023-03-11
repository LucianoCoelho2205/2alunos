from controller import salvar,listar,listarpessoa,deletarpessoa #importando funções de outro arquivo

def menu():
    menu = 1

    while(menu !=0):
        
        menu = int(input("1-Fazer Cadastro\n2-Relatório Nomes\n3-Relatorio por Pessoa\n4-Deletar\n0-Para Sair\n>>>>>>"))

        match menu:

            case 1:
                pessoa = {}
                pessoa['nome'] = input("Digite o nome do cliente>>> ")
                pessoa['carro'] = input("Digite o modelo do carro>>> ")
                pessoa["ano"] = int(input("Digite o ano do carro>>> "))
                pessoa["telefone"] = input("Digite o telefone do cliente>>> ")
                pessoa["pecas"] = input("Quais foram a peças trocadas>>> ")

                salvar(pessoa)

            case 2:
                  listar()

            case 3:
                  pessoa = input("Digite o que voce deseja buscar>>> ")
                  listarpessoa(pessoa)

            case 4:
                  pessoa = input("Digite o que voce deseja excluir>>> ")
                  deletarpessoa(pessoa)



            

    