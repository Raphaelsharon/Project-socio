from class_banco_de_dados import Tabela_socios as Ts

class Socios(Ts):
    
    conexao = Ts.ConecaoBanco()
    #adicionar socios a tabela
    def add_socio(): # OK!
        try:        
            id_socio = str(input("Informe o ID do sócio: "))
            nome = str(input("Informe o nome do sócio: "))
            data_nascimento = str(input("Informe a data de nascimento do usuário: "))
            cpf = str(input("Informe o CPF do usuário: "))
            rg = str(input("Informe o RG do usuário: "))
            nit = str(input("Informe o NIT do usuário: "))
            cei = str(input("Informe o CEI do usuário: "))
            email = str(input("Informe o email do usuário: "))
            telefone = str(input("Informe o telefone do usuário: "))
            cidade = str(input("Informe a cidade do usuário: "))
            bairro = str(input("Informe o bairro do usuário: "))
            numero = str(input("Informe o numero do resideiro do usuário: "))
            complemento = str(input("Informe o complemento do resideiro do usuário: "))
            
            #criar_tabela = Ts.CriaTabela_socios(conexao)
            insert_socios = Ts.InsertDados_socios(Socios.conexao, id_socio,nome, data_nascimento,cpf,rg,nit,cei,email,telefone,cidade,bairro,numero,complemento)
            print("Socio adicionado")
        except ValueError as ex:
            print("Valor invalido!")
            print(ex)
    #Atualiza um dado 
    def up_dados(): #OK!
        try:
            id_socio = str(input("Informe o ID do socio que dejesa alterar alguma informação: "))
            dado = str(input("Digite o nome do dado que deseja alterar: "))
            up = str(input(f"Informe o novo {dado}: "))
            upgrade_dados = Ts.UpdateDados_socios(Socios.conexao,id_socio, dado, up)
        except:
            print("Valor invalido!")
            
    #Deleta socio
    def clear_socios(): #OK!
        try:
            id_socio = str(input("Digite o ID do socio que deseja excluir: "))
            clear_dados = Ts.ClearDados_socios(Socios.conexao, id_socio)
        except:
            print("Valor invalido!")
    
    #Lista um socio
    def list_unic_socio():
        try:
            list_dados = Ts.SelectDados_socio(Socios.conexao)
        except:
            print("Valor invalido!")
            
    #Lista todos os socios
    def list_socios(): #OK!
        try:
            list_dados = Ts.SelectTodosDados_socios(Socios.conexao)
        except:
            print("Valor invalido!")

