import sqlite3 
from sqlite3 import Error

class Tabela_socios:
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
    def CriaTabela_socios(conexao):
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
        except Error as ex:
            print("Erro ao criar tabela!")
            print(ex)
        finally:
            print("Tabela criada")
            
    #Inserir dados na tabela
    def InsertDados_socios(conexao,id,nome,cpf,rg,nit,cei,email,telefone,cidade,bairro,numero,complemento):
        try:
            
            inserir_dados = """INSERT INTO SOCIOS 
                (ID,NOME,CPF,RG,NIT,CEI,EMAIL,TELEFONE,CIDADE,BAIRRO,NUMERO,COMPLEMENTO)
            VALUES('"""+id+"""','"""+nome+"""','"""+cpf+"""','"""+rg+"""','"""+nit+"""','"""+cei+"""','"""+email+"""','"""+telefone+"""','"""+cidade+"""','"""+bairro+"""','"""+numero+"""','"""+complemento+"""')
            """
            
            cursor = conexao.cursor()
            cursor.execute(inserir_dados)
            conexao.commit()    
        except Error as ex:
            print("Erro ao inserir os dados!")
            print(ex)
        finally:
            print("Dados cadastrados")
    #Excluir Dados
    def ClearDados_socios(conexao, id_pessoa):
        try:
            if id_pessoa:
                exluir_dados = """DELETE FROM SOCIOS WHERE ID="""+id_pessoa+""""""
                cursor = conexao.cursor()
                cursor.execute(exluir_dados)
                conexao.commit()
        except Error as ex:
            print("Erro ao excluir os dados!")
            print(ex)
        finally:
            print("Dados deletados")

    #Alterar Dados
    def UpdateDados_NOME_socios(conexao, id_pessoa):
        try:
            update_dados = """UPDATE SOCIOS SET NOME='RAPHAEL' WHERE ID="""+id_pessoa+""""""
            cursor = conexao.cursor()
            cursor.execute(update_dados)
            conexao.commit()
        except Error as ex:
            print("Erro ao atualizar os dados!")
            print(ex)
        finally:
            print("Nome atualizado")
            
    def UpdateDados_CPF_socios(conexao, id_pessoa):
        try:
            update_dados = """UPDATE SOCIOS SET CPF='109.378.665-55' WHERE ID="""+id_pessoa+""""""
            cursor = conexao.cursor()
            cursor.execute(update_dados)
            conexao.commit()
        except Error as ex:
            print("Erro ao atualizar os dados!")
            print(ex)
        finally:
            print("CPF atualizado")
    
    def UpdateDados_RG_socios(conexao, id_pessoa):
        try:
            update_dados = """UPDATE SOCIOS SET RG='22.5785.444-48' WHERE ID="""+id_pessoa+""""""
            cursor = conexao.cursor()
            cursor.execute(update_dados)
            conexao.commit()
        except Error as ex:
            print("Erro ao atualizar os dados!")
            print(ex)
        finally:
            print("RG atualizado")
    
    def UpdateDados_NIT_socios(conexao, id_pessoa):
        try:
            update_dados = """UPDATE SOCIOS SET NIT='11.444.858-50' WHERE ID="""+id_pessoa+""""""
            cursor = conexao.cursor()
            cursor.execute(update_dados)
            conexao.commit()
        except Error as ex:
            print("Erro ao atualizar os dados!")
            print(ex)
        finally:
            print("NIT atualizado")
    
    def UpdateDados_CEI_socios(conexao, id_pessoa):
        try:
            update_dados = """UPDATE SOCIOS SET CEI='999.874.4111-45' WHERE ID="""+id_pessoa+""""""
            cursor = conexao.cursor()
            cursor.execute(update_dados)
            conexao.commit()
        except Error as ex:
            print("Erro ao atualizar os dados!")
            print(ex)
        finally:
            print("CEI atualizado")
            
    def UpdateDados_EMAIL_socios(conexao, id_pessoa):
        try:
            update_dados = """UPDATE SOCIOS SET EMAIL='batistaraphael@gmail.com' WHERE ID="""+id_pessoa+""""""
            cursor = conexao.cursor()
            cursor.execute(update_dados)
            conexao.commit()
        except Error as ex:
            print("Erro ao atualizar os dados!")
            print(ex)
        finally:
            print("EMAIL atualizado")
    
    def UpdateDados_TELEFONE_socios(conexao, id_pessoa):
        try:
            update_dados = """UPDATE SOCIOS SET TELEFONE='(75) 98886-0451' WHERE ID="""+id_pessoa+""""""
            cursor = conexao.cursor()
            cursor.execute(update_dados)
            conexao.commit()
        except Error as ex:
            print("Erro ao atualizar os dados!")
            print(ex)
        finally:
            print("TELEFONE atualizado")

    def UpdateDados_CIDADE_socios(conexao, id_pessoa):
        try:
            update_dados = """UPDATE SOCIOS SET CIDADE='Cruz das Almas' WHERE ID="""+id_pessoa+""""""
            cursor = conexao.cursor()
            cursor.execute(update_dados)
            conexao.commit()
        except Error as ex:
            print("Erro ao atualizar os dados!")
            print(ex)
        finally:
            print("CIDADE atualizado")
    
    def UpdateDados_BAIRRO_socios(conexao, id_pessoa):
        try:
            update_dados = """UPDATE SOCIOS SET BAIRRO='inocoop' WHERE ID="""+id_pessoa+""""""
            cursor = conexao.cursor()
            cursor.execute(update_dados)
            conexao.commit()
        except Error as ex:
            print("Erro ao atualizar os dados!")
            print(ex)
        finally:
            print("BAIRRO atualizado")
    
    def UpdateDados_NUMERO_socios(conexao, id_pessoa):
        try:
            update_dados = """UPDATE SOCIOS SET NUMERO='35' WHERE ID="""+id_pessoa+""""""
            cursor = conexao.cursor()
            cursor.execute(update_dados)
            conexao.commit()
        except Error as ex:
            print("Erro ao atualizar os dados!")
            print(ex)
        finally:
            print("NUMERO atualizado")

    def UpdateDados_COMPLEMENTO_socios(conexao, id_pessoa):  
        try:
            update_dados = """UPDATE SOCIOS SET COMPLEMENTO='Casa' WHERE ID="""+id_pessoa+""""""
            cursor = conexao.cursor()
            cursor.execute(update_dados)
            conexao.commit()
        except Error as ex:
            print("Erro ao atualizar os dados!")
            print(ex)
        finally:
            print("COMPLEMENTO atualizado")
    
    #Selecionar Dados
    def SelectDados_socios(conexao,id_pessoa):
    
        select_dados = """SELECT * FROM SOCIOS WHERE ID="""+id_pessoa+""""""
        cursor = conexao.cursor()
        cursor.execute(select_dados)
        resultado = cursor.fetchall()
        return resultado #Necessario printar

class Tabela_Anos(Tabela_socios):
    #subistituir '2024' por uma variavel para que assim nao necessitar da repedição do codigo para cada ano
    def CriaTabela_2024(conexao):
        try:
            criar_tabela = """CREATE TABLE IF NOT EXISTS '2024' (
                            Socio_id INTEGER PRIMARY KEY,
                            JANEIRO TEXT,
                            FEVEREIRO TEXT,
                            MARÇO TEXT,
                            ABRIL TEXT,
                            MAIO TEXT,
                            JUNHO TEXT,
                            JULHO TEXT,
                            AGOSTO TEXT,
                            SETEMBRO TEXT,
                            OUTUBRO TEXT,
                            NOVEMBRO TEXT,
                            DEZEMBRO TEXT,
                            FOREIGN KEY (Socio_id) REFERENCES SOCIOS(id)
                            )"""
                            
            cursor = conexao.cursor()  
            cursor.execute(criar_tabela) 
            print("Tabela criada")
        except Error as ex:
            print("Erro ao criar tabela!")
            print(ex)
    
    
    def InsertDados_2024(conexao, socio_id):
        try:
            inserir_dados = """INSERT INTO '2024' 
                (Socio_id, JANEIRO, FEVEREIRO, MARÇO, ABRIL, MAIO, JUNHO, JULHO, AGOSTO, SETEMBRO, OUTUBRO, NOVEMBRO, DEZEMBRO)
                VALUES (?, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)"""
            cursor = conexao.cursor()
            cursor.execute(inserir_dados, (socio_id,))
            conexao.commit()    
            print("Dados cadastrados")
        except Error as ex:
            print("Erro ao inserir os dados!")
            print(ex)
            
    def VisualizarDados_2024(conexao):
        try:
            consulta = "SELECT * FROM '2024'"
            cursor = conexao.cursor()
            cursor.execute(consulta)
            linhas = cursor.fetchall()
            
            print("Dados da tabela '2024':")
            for linha in linhas:
                print(linha)
        except Error as ex:
            print("Erro ao visualizar os dados!")
            print(ex)
            
    
#testes
test_conect = Tabela_socios.ConecaoBanco()
#test_tabela = Banco_de_Dados.CriaTabela(test_conect)
#test_insert = Banco_de_Dados.InsertDados(test_conect, '200','ph','999999999','5555555555','888888888','1111111111','ph1@gmail.com','(75)99999997','Maragogo','RUA DO RIO','05','casa')
#test_clear = Banco_de_Dados.ClearDados(test_conect, '201')
#test_updade = Banco_de_Dados.UpdateDados_NOME(test_conect, '201')
#test_select = Banco_de_Dados.SelectDados(test_conect, '201'), print(test_select)
#test_pagamento = Tabela_Anos.CriaTabela_2024(test_conect)
test_pagamento_insert = Tabela_Anos.InsertDados_2024(test_conect,'201')
test_pagamento_visualizar = Tabela_Anos.VisualizarDados_2024(test_conect)

#test_pagamento = Tabela_Anos.CriaTabela_2023(test_conect)
test_pagamento_insert = Tabela_Anos.InsertDados_2023(test_conect,'201')
test_pagamento_visualizar = Tabela_Anos.VisualizarDados_2023(test_conect)