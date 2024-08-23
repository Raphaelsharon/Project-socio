import sqlite3 
from sqlite3 import Error

class Banco_de_Dados:
    #Criar conexão
    def ConecaoBanco(): 
        caminho = "C:\\Users\PH\\Documents\\Projetos Pessoais\\Socios (sindcato)\\Codigo\\caminho_banco_de_dados"
        conexao = None
        try:
            conexao = sqlite3.connect(caminho)
        except Error as ex:
            print("Conexão falhou!")
            print(ex)
        return conexao

    #Criar tabela, os dados como id, cpf, nit, cei, telefone e email so podem existir um por pessoa 
    def CriaTabela(conexao):
        try:
            criar_tabela = """CREATE TABLE SOCIOS(
                            ID INTEGER PRIMARY KEY,
                            NOME TEXT,
                            CPF VARCHAR(15) UNIQUE,
                            RG VARCHAR(20) UNIQUE,
                            NIT VARCHAR(20) UNIQUE,
                            CEI VARCHAR(20) UNIQUE,
                            EMAIL VARCHAR(20) UNIQUE,
                            TELEFONE VARCHAR(15) UNIQUE,
                            CIDADE TEXT,
                            BAIRRO TEXT,
                            NUMERO VARCHAR(4),
                            COMPLEMENTO VARCHAR(15)
                            )"""
            cursor = conexao.cursor()  
            cursor.execute(criar_tabela)
            print("Tabela criada")
        except Error as ex:
            print("Erro ao criar tabela!")
            print(ex)
    #Inserir dados na tabela
    def InsertDados(conexao,id,nome,cpf,rg,nit,cei,email,telefone,cidade,bairro,numero,complemento):
        try:
            
            inserir_dados = """INSERT INTO SOCIOS 
                (ID,NOME,CPF,RG,NIT,CEI,EMAIL,TELEFONE,CIDADE,BAIRRO,NUMERO,COMPLEMENTO)
            VALUES('"""+id+"""','"""+nome+"""','"""+cpf+"""','"""+rg+"""','"""+nit+"""','"""+cei+"""','"""+email+"""','"""+telefone+"""','"""+cidade+"""','"""+bairro+"""','"""+numero+"""','"""+complemento+"""')
            """
            
            cursor = conexao.cursor()
            cursor.execute(inserir_dados)
            conexao.commit()
            print("Dados cadastrados")
        except Error as ex:
            print("Erro ao inserir os dados!")
            print(ex)
    
    #Selecionar Dados
    def SelectDados():
        pass

    #Alterar dados
    def ChangeDados():
        pass
    
    def ClearDados():
        pass
    
#testes
test_conect = Banco_de_Dados.ConecaoBanco()
#test_tabela = Banco_de_Dados.CriaTabela(test_conect)
test_insert = Banco_de_Dados.InsertDados(test_conect, '201','ph','9979999999','55555555855','8888818888','11111111111','ph1@gmail.com','(75)99999997','Maragogo','RUA DO RIO','05','casa')