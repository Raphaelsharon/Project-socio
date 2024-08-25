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
                            DATA_DE_NASCIMENTO TEXT,
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
    def InsertDados_socios(conexao,id,nome,data_nascimento,cpf,rg,nit,cei,email,telefone,cidade,bairro,numero,complemento):
        try:
            
            inserir_dados = """INSERT INTO SOCIOS 
                (ID,NOME,DATA_DE_NASCIMENTO,CPF,RG,NIT,CEI,EMAIL,TELEFONE,CIDADE,BAIRRO,NUMERO,COMPLEMENTO)
            VALUES('"""+id+"""','"""+nome+"""','"""+data_nascimento+"""','"""+cpf+"""','"""+rg+"""','"""+nit+"""','"""+cei+"""','"""+email+"""','"""+telefone+"""','"""+cidade+"""','"""+bairro+"""','"""+numero+"""','"""+complemento+"""')
            """
            
            cursor = conexao.cursor()
            cursor.execute(inserir_dados)
            conexao.commit()    
        except Error as ex:
            print("Erro ao inserir os dados!")
            print(ex)
        #finally:
            #print("Dados cadastrados")
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
            print(f"Socio {id_pessoa} deletado")

    #Alterar Dados
    def UpdateDados_socios(conexao, id_pessoa, dado, update):
        try:
            up_dados = dado.upper()
            update_dados = f"""UPDATE SOCIOS SET '{up_dados}'='{update}' WHERE ID="""+id_pessoa+""""""
            cursor = conexao.cursor()
            cursor.execute(update_dados)
            conexao.commit()
        except Error as ex:
            print("Erro ao atualizar os dados!")
            print(ex)
        finally:
            print(f"{dado} atualizado")
     
    #Selecionar Dados
    def SelectDados_socio(conexao,id_pessoa):
    
        select_dados = """SELECT * FROM SOCIOS WHERE ID="""+id_pessoa+""""""
        cursor = conexao.cursor()
        cursor.execute(select_dados)
        resultado = cursor.fetchall()
        print(f"Dados do id {id_pessoa}: ")
        for linha in resultado:
            print(linha)
        return resultado #Necessario printar
    def SelectTodosDados_socios(conexao):
    
        select_dados = """SELECT * FROM SOCIOS"""
        cursor = conexao.cursor()
        cursor.execute(select_dados)
        resultado = cursor.fetchall()
        print("Dados da tabela 'Socios': ")
        for linha in resultado:
            print(linha)
        return resultado #Necessario printar

class Tabela_Anos(Tabela_socios):

    def CriaTabela_ano(conexao, ano):
        try:
            criar_tabela = f"""CREATE TABLE IF NOT EXISTS '{ano}' (
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
            print(f"Tabela '{ano}' criada")
        except Exception as ex:
            print("Erro ao criar tabela!")
            print(ex)
    
    
    def InsertDados_ano(conexao, socio_id, ano):
        try:
            inserir_dados = f"""INSERT INTO '{ano}' 
                (Socio_id, JANEIRO, FEVEREIRO, MARÇO, ABRIL, MAIO, JUNHO, JULHO, AGOSTO, SETEMBRO, OUTUBRO, NOVEMBRO, DEZEMBRO)
                VALUES (?, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)"""
            cursor = conexao.cursor()
            cursor.execute(inserir_dados, (socio_id,))
            conexao.commit()    
            print(f"Dados cadastrados na tabela '{ano}'")
        except Exception as ex:
            print("Erro ao inserir os dados!")
            print(ex)
            
    def SelectTodosDados_ano(conexao, ano):
        try:
            consulta = f"SELECT * FROM '{ano}'"
            cursor = conexao.cursor()
            cursor.execute(consulta)
            linhas = cursor.fetchall()
            
            print(f"Dados da tabela '{ano}':")
            for linha in linhas:
                print(linha)
        except Exception as ex:
            print("Erro ao visualizar os dados!")
            print(ex)
        
    def SelectIdDados_ano(conexao, ano,socio_id):
        try:
            consulta = f"SELECT * FROM '{ano}' WHERE Socio_id={socio_id}"
            cursor = conexao.cursor()
            cursor.execute(consulta)
            linhas = cursor.fetchall()
            
            print(f"Dados do socios '{socio_id}' do ano '{ano}':")
            for linha in linhas:
                print(linha)
        except Exception as ex:
            print("Erro ao visualizar os dados!")
            print(ex)
        
    def UpdateDados_ano(conexao, ano, id_socio, **meses_valores):
        try:
            # Criar string de colunas a serem atualizadas
            colunas = ', '.join([f"{mes} = ?" for mes in meses_valores.keys()])
            valores = list(meses_valores.values())
            valores.append(id_socio)

            update_dados = f"""UPDATE '{ano}' 
                               SET {colunas} 
                               WHERE Socio_id = ?"""
                               
            cursor = conexao.cursor()
            cursor.execute(update_dados, valores)
            conexao.commit()
            print(f"Tabela '{ano}' atualizada para o sócio ID {id_socio}")
        except Exception as ex:
            print("Erro ao atualizar os dados!")
            print(ex)
            
    def MesesComNull(conexao, ano, socio_id):
        try:
            # Lista de todos os meses
            meses = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", 
                    "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"]
            
            # Consulta para buscar os valores dos meses para o sócio específico
            consulta = f"SELECT {', '.join(meses)} FROM '{ano}' WHERE Socio_id = ?"
            
            cursor = conexao.cursor()
            cursor.execute(consulta, (socio_id,))
            resultado = cursor.fetchone()
            
            if resultado:
                # Verificar quais meses têm valor NULL
                meses_com_null = [mes for mes, valor in zip(meses, resultado) if valor is None]
                return meses_com_null
            else:
                print(f"Não foram encontrados dados para o socio_id {socio_id} na tabela '{ano}'.")
                return []
        except Exception as ex:
            print("Erro ao buscar meses com valores NULL!")
            print(ex)
            return []

#sempre usar aspas simples nos 
'''
#testes
conexao = Tabela_socios.ConecaoBanco()
test_tabela = Tabela_socios.CriaTabela_socios(conexao)
test_insert = Tabela_socios.InsertDados_socios(conexao, '200','ph','29/01/2005','999999999','5555555555','888888888','1111111111','ph1@gmail.com','(75)99999997','Maragogo','RUA DO RIO','05','casa')
#test_clear = Banco_de_Dados.ClearDados(test_conect, '200')
#test_updade = Banco_de_Dados.UpdateDados_NOME(test_conect, '200')

#test_pagamento = Tabela_Anos.CriaTabela_2023(test_conect)

# Criando a tabela para o ano de 2023
tabela = Tabela_Anos()
tabela.CriaTabela_ano(conexao, 2023)

# Inserindo dados para um sócio na tabela de 2023
tabela.InsertDados_ano(conexao, '200', 2023)
test_select = Tabela_socios.SelectDados_socios(conexao, '200')
#Visualizando dados da tabela de 2023
tabela.SelectTodosDados_ano(conexao, 2023)
tabela.SelectIdDados_ano(conexao, 2023, '200')
# Atualizando os dados do sócio na tabela de 2023
tabela.UpdateDados_ano(conexao, 2023, '200', JANEIRO="Pago", FEVEREIRO="Pago", MARÇO="Pago")
tabela.SelectTodosDados_ano(conexao, 2023)
tabela.SelectIdDados_ano(conexao, 2023, '200')
# Supondo que a conexão com o banco de dados já esteja estabelecida e a tabela de 2023 exista:
a = '200'
meses_nulos = Tabela_Anos.MesesComNull(conexao, 2023, a)
meses = len(meses_nulos)
soma = meses*12.00
print(f"Meses nao pagos do sócio ID {a} em 2023: {meses_nulos}\n cujo total é {meses} e o valor a pagar é {soma}")
'''