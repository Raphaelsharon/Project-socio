from class_banco_de_dados import Tabela_Anos as Ta

class Valida_pagamendo(Ta):
    
    conexao = Ta.ConecaoBanco()
    
    #Criar tabela de um determinado ano
    def creat_ano(): #OK!
        ano = input("Informe o ano da tabela que dejesa criar: : ")
        tabela_ano = Ta.CriaTabela_ano(Valida_pagamendo.conexao, ano)
   
   #adiciona o socio a tabela do ano
    def add_ano(): #OK!     
        id_socio = input("Informe o id do socio que deseja inserir na tabela: ")
        ano = input("Qual ano deseja atualizar: ")
        insert = Ta.InsertDados_ano(Valida_pagamendo.conexao, id_socio, ano)

    def up_ano():
        pass