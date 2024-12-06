# Seção p/ importação de bibliotecas
#-----------------------------------------------------------#
import sys
from datetime import datetime
import os
#-----------------------------------------------------------#

# Mensagem de introdução ao programa
#-----------------------------------------------------------#
print("")
print("Seja bem-vindo ao criador de Ordens de Serviço!")
print("")
#-----------------------------------------------------------#


# INÍCIO PROGRAMAÇÃO DATA
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Início da programação da data de abertura da ordem de serviço.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Inserção de valores da data 
#------------------------------------------------------------------------------------------------------------------------#
print("Insira a data referente à realização da OS no formato dd/mm/aa ou dd/mm/aaaa.")

# Início do loop while para reinserção da data, caso solicitado
#-----------------------------------------------------------#
while True:
#-----------------------------------------------------------#

    print("")
    print("__/__/__")

    print("")
    resp_dia = int(input("Insira o dia: "))
    print("")

    print(f"dd/__/__")

    print("")
    resp_mes = int(input("Insira o mês: "))
    print("")

    print(f"dd/mm/__")

    print("")
    resp_ano = int(input("Insira o ano: "))
    print("")
#------------------------------------------------------------------------------------------------------------------------#

# Verificação de ano bissexto
#-----------------------------------------------------------#
    def ano_bissexto(resp_ano):
        if (resp_ano % 4 == 0 and resp_ano % 100 != 0) or (resp_ano % 400 == 0):
            return True
        else:
            return False
#-----------------------------------------------------------#

# Correção dos valores da data
#-----------------------------------------------------------#
    if resp_dia < 10 and resp_mes < 10:
        fim_ano = (f"0{resp_dia}/0{resp_mes}/{resp_ano}")
    elif resp_dia < 10:
        fim_ano = (f"0{resp_dia}/{resp_mes}/{resp_ano}")
    elif resp_mes < 10:
        fim_ano = (f"{resp_dia}/0{resp_mes}/{resp_ano}")
    else:
        fim_ano = (f"{resp_dia}/{resp_mes}/{resp_ano}")
#-----------------------------------------------------------#

# Verificação do formato e concordância do ano (aa/aaaa)
#-----------------------------------------------------------#
    tamanho_ano = len(str(resp_ano))

    if tamanho_ano > 2 and tamanho_ano < 4:
        print ("Formatação do ano inválida. Inserir padrão dd/mm/aaaa ou dd/mm/aaaa.")
        sys.exit()
    elif tamanho_ano < 2:
        print ("Formatação do ano inválida. Inserir padrão dd/mm/aaaa ou dd/mm/aaaa.")
        sys.exit()
    elif tamanho_ano > 4:
        print ("Formatação do ano inválida. Inserir padrão dd/mm/aaaa ou dd/mm/aaaa.")
        sys.exit()
    elif tamanho_ano == 2 and resp_ano > 24:
        print ("Data superior ao ano atual.")
        sys.exit()
    elif tamanho_ano == 4 and resp_ano > 2024:
        print ("Data superior ao ano atual.")
        sys.exit()  
#-----------------------------------------------------------#

# Verificação de coerência com a data
#-----------------------------------------------------------#
    if resp_dia < 1 or resp_dia > 31:
        print("Esta data é inválida.") 
        sys.exit()
    elif resp_mes < 1 or resp_mes > 12: 
        print("Este mês é inválido.") 
        sys.exit()
    elif resp_mes == 2 and resp_dia > 29: 
        print("Data inválida para fevereiro.") 
        sys.exit()
    elif resp_mes == 2 and resp_dia == 29 and not ano_bissexto(resp_ano): 
        print("Data inválida para ano não bissexto.") 
        sys.exit()
    elif resp_mes == 4 and resp_dia > 30 or resp_mes == 6 and resp_dia > 30 or resp_mes == 9 and resp_dia > 30 or resp_mes == 11 and resp_dia > 30:
        print("Data inválida para o mês inserido.") 
        sys.exit()
#-----------------------------------------------------------#

# Confirmação de inserção da data
#------------------------------------------------------------------------------------------------------------------------#
    
    print(f"Data inserida: {fim_ano} | Isto está correto?")

# Loop while para reinserção da confirmação, caso input errado
#-----------------------------------------------------------#
    while True:
#-----------------------------------------------------------#

        print("Digite 'S' para confimar e 'N' para reescrever.")
        print("")
        confirmacao_mes = input("").upper()
        print("")

        if confirmacao_mes == "S":
            break
        elif confirmacao_mes == "N":
            print("")
            print("Você poderá colocar a data novamente à seguir.")
            break
        else:
            print("")
            print("O valor inserido é inválido. Escolha-o novamente.")
            print("")

    if confirmacao_mes == "S":
        break
#------------------------------------------------------------------------------------------------------------------------#


# INÍCIO PROGRAMAÇÃO NOME DO CLIENTE
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Início da programação da inserção do nome do cliente. 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Inserção do nome do cliente (físico/jurídico)
#------------------------------------------------------------------------------------------------------------------------#

print ("Insira o nome do cliente abaixo:")
print("")

# Início do loop while para reinserção do nome do cliente, caso solicitado
#-----------------------------------------------------------#
while True:
#-----------------------------------------------------------#
    
    resp_cliente = input("- ")

#------------------------------------------------------------------------------------------------------------------------#

# Início do loop while para reinserção da confirmação, caso input errado
#-----------------------------------------------------------#
    while True:
#-----------------------------------------------------------#

        print("")
        print(f"O nome do cliente é {resp_cliente} | Isto está correto?")
        print("Digite 'S' para confimar e 'N' para reescrever.")
        print("")
        confirmacao_cliente = input("").upper()
        print("")

        if confirmacao_cliente == "S":
            break
        elif confirmacao_cliente == "N":
            print("Insira o nome novamente, abaixo:")
            print("")
            break
        else:
            print("")
            print("Valor inserido inválido.")
            print("")
    
    if confirmacao_cliente == "S":
        break
#------------------------------------------------------------------------------------------------------------------------#


# INÍCIO PROGRAMAÇÃO ENDEREÇO DO CLIENTE
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Início da programação da inserção do endereço do ciente.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Inserção do endereço do cliente
#------------------------------------------------------------------------------------------------------------------------#

print("Insira o endereço do local:")
print("")

# Início do loop while para reinserção do endereço do cliente, caso solicitado
#-----------------------------------------------------------#
while True:
#-----------------------------------------------------------#

    resp_endereco = input("- ")

# Início do loop while para reinserção do endereço do cliente, caso solicitado
#-----------------------------------------------------------#
    while True:
#-----------------------------------------------------------#

        print("")
        print(f"O endereço do cliente é: {resp_endereco} | Isto está correto?")
        print("Digite 'S' para confimar e 'N' para reescrever.")
        print("")
        confirmacao_endereco = input("").upper()
        print("")

        if confirmacao_endereco == "S":
                break
        elif confirmacao_endereco == "N":
                print("Insira o endereço novamente, abaixo:")
                print("")
                break
        else:
                print("")
                print("Valor inserido inválido.")
                print("")
    
    if confirmacao_endereco == "S":
        break
#------------------------------------------------------------------------------------------------------------------------#


# INÍCIO PROGRAMAÇÃO UF
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Início da programação da inserção da unidade federativa.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


print ("Insira a sigla da UF de onde o serviço foi prestado:")

# Início do loop while para reinserção da UF, caso solicitado
#-----------------------------------------------------------#
while True:
#-----------------------------------------------------------#

# Inserção nome da sigla da UF
#---------------------------------------------------------#
    resp_uf = input("- ").upper()
#-----------------------------------------------------------#

# Criação de lista verificadora das UFs
#-----------------------------------------------------------#
    def escolha_uf(resp_uf):
        if  resp_uf == "SP" or resp_uf == "AL" or resp_uf == "AC" or resp_uf == "AP" or resp_uf == "AM" or resp_uf == "BA" or resp_uf == "CE" or resp_uf == "DF" or resp_uf == "ES" or resp_uf == "GO" or resp_uf == "MA" or resp_uf == "MT" or resp_uf == "MS" or resp_uf == "MG" or resp_uf == "PA" or resp_uf == "PB" or resp_uf == "PR" or resp_uf == "PE" or resp_uf == "PI" or resp_uf == "RH" or resp_uf == "RN" or resp_uf == "RS" or resp_uf == "RO" or resp_uf == "RR" or resp_uf == "SC" or resp_uf == "SP" or resp_uf == "SE" or resp_uf == "TO":
            return True
        else:
            return False
#-----------------------------------------------------------#   

    confirmacao_uf = ""

    while True:

# Pergunta e registro de confirmação de inserção das UFs
#-----------------------------------------------------------#
        if escolha_uf(resp_uf):
            print("")
            print(f"A UF selecionada é {resp_uf} | Isto está correto?")
            print("Digite 'S' para 'Sim' e 'N' para não: ")
            print("")
            confirmacao_uf = input("").upper()

            if confirmacao_uf =="S":
                break

            elif confirmacao_uf == "N":
                print("")
                print("Você poderá colocar a UF novamente à seguir.")
                print("")
                break
            
            else: 
                print("")
                print("O valor inserido é inválido. Escolha-o novamente.")
                print("")

        elif not escolha_uf(resp_uf): 
            print("")
            print("UF inválida, insira uma das UFs listadas abaixo:")
            print("")
            print("AC, AL, AP, AM, BA, CE, DF, ES, GO, MA, MT, MS, MG, PA, PB, PR, PE, PI, RJ, RN, RS, RO, RR, SC, SP, SE, TO.")
            print("")
            break

    if confirmacao_uf == "S":
        break
#-----------------------------------------------------------#        


# INÍCIO PROGRAMAÇÃO TELEFONE DO CLIENTE
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Início da programação da inserção do telefone do cliente. 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Inserção do número de telefone
#-----------------------------------------------------------#

print("")
print("Insira o número de telefone do cliente com DDD no padrão (dd) nnnnn-nnnn")
print("")
print("Obs: Não coloque espaços ou caracteres especiais!")
print("")

# Início do loop while para reinserção do telefone, caso solicitado no final.
#-----------------------------------------------------------#
while True:
#-----------------------------------------------------------#

# Início do loop while para reinserção do telefone, caso tamanho errado.
#-----------------------------------------------------------#
    while True:
#-----------------------------------------------------------#

        resp_telefone = int(input("- "))
        print("")

#-----------------------------------------------------------#

# Transformação do número de telefone em string p/ formatação
#-----------------------------------------------------------#
        resp_telefone_str = str(resp_telefone)
#-----------------------------------------------------------#

# Verificação de tamanho da string
#-----------------------------------------------------------#
        if len(resp_telefone_str) != 11:
            print("Número de telefone inválido! Insira-o novamente abaixo.")
            print("")
        else:
            break
#-----------------------------------------------------------#

# Formatação do telefone
#-----------------------------------------------------------#
    resp_telefone_str = (f"({resp_telefone_str[0:2]}) {resp_telefone_str[2:7]}-{resp_telefone_str[7:11]}")
#-----------------------------------------------------------#

# Início do loop while para reinserção do endereço do cliente, caso solicitado
#-----------------------------------------------------------#
    while True:
#-----------------------------------------------------------#

        print("")
        print(f"O endereço telefone do cliente é: {resp_telefone_str} | Isto está correto?")
        print("Digite 'S' para confimar e 'N' para reescrever.")
        print("")
        confirmacao_telefone = input("").upper()
        print("")

        if confirmacao_telefone == "S":
                break
        elif confirmacao_telefone == "N":
                print("Insira o endereço novamente, abaixo:")
                print("")
                break
        else:
                print("")
                print("Valor inserido inválido.")
                print("")
    
    if confirmacao_telefone == "S":
        break
#------------------------------------------------------------------------------------------------------------------------#


# INÍCIO PROGRAMAÇÃO TIPO DE ATENDIMENTO
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Início da programação da inserção do tipo de atendimento prestado ao cliente. 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Início do loop while para reinserção do tipo de atendimento, caso solicitado
#-----------------------------------------------------------#
while True:
#-----------------------------------------------------------#

# Início do loop while para reinserção do tipo de atendimento, caso solicitado
#-----------------------------------------------------------#
    while True:
#-----------------------------------------------------------#

# Inserção do tipo de atendimento
#-----------------------------------------------------------#
        print("")
        print("Insira o número correspondente ao tipo de atendimento: ")
        print("")
        print("1- Contratual")
        print("")
        print("2- Avulso")
        print("")
        resp_tipo_atendimento = input("")
        print("")
#-----------------------------------------------------------#

# Formatação da variável para valores da escolha
#-----------------------------------------------------------#
        if resp_tipo_atendimento == "1":
            resp_tipo_atendimento = ("Contratual")
            break
        elif resp_tipo_atendimento == "2":
            resp_tipo_atendimento = ("Avulso")
            break
        else: 
            print("")
            print("Valor digitado inválido.")
            print("")
            print("Insira o valor novamente à seguir.")
            print("")
#-----------------------------------------------------------#

# Início do loop while para reinserção da confirmação do tipo de atendimento.
#-----------------------------------------------------------#
    while True:
#-----------------------------------------------------------#

        print("")
        print(f"O tipo de atendimento prestado é: {resp_tipo_atendimento} | Isto está correto?")
        print("Digite 'S' para confimar e 'N' para reescrever.")
        print("")
        confirmacao_tipo_atendimento = input("").upper()
        print("")

        if confirmacao_tipo_atendimento == "S":
                break
        elif confirmacao_tipo_atendimento == "N":
                print("Insira o endereço novamente, abaixo:")
                print("")
                break
        else:
                print("")
                print("Valor inserido inválido.")
                print("")
    
    if confirmacao_tipo_atendimento == "S":
        break
#------------------------------------------------------------------------------------------------------------------------#


# INÍCIO PROGRAMAÇÃO TIPO DE EQUIPAMENTO
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Início da programação da inserção do tipo de equipamento do cliente. 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Início do loop while para reinserção do tipo de equipamento, caso valor inválido
#-----------------------------------------------------------#
while True:
#-----------------------------------------------------------#

# Início do loop while para reinserção do tipo de equipamento, caso solicitado
#-----------------------------------------------------------#
    while True:
#-----------------------------------------------------------#

# Inserção de tipo de equipamento
#-----------------------------------------------------------#
        print("")
        print("Insira o número correspondente ao tipo de equipamento: ")
        print("")
        print("1- Desktop")
        print("")
        print("2- Notebook")
        print("")
        print("3- Outros")
        print("")
        resp_tipo_equipamento = (input(""))
        print("")
#-----------------------------------------------------------#

# Correção de valores pós escolha
#-----------------------------------------------------------#
        if resp_tipo_equipamento == "1":
            resp_tipo_equipamento = "Desktop"
            break
        elif resp_tipo_equipamento == "2":
            resp_tipo_equipamento = "Notebook"
            break
        elif resp_tipo_equipamento == "3":
            print("")
            resp_tipo_equipamento = resp_tipo_equipamento = input("Insira outra categoria de equipamento: ")
            print("")
            break
        else:
            print("")
            print("Este valor é inválido.")
            print("")
            print("Verifique as opções abaixo e especifique o valor desejado")
            print("")
#-----------------------------------------------------------#

# Início do loop while para reinserção da confirmação de escolha.
#-----------------------------------------------------------#
    while True:
#-----------------------------------------------------------#

        print("")
        print(f"O tipo de atendimento prestado é: {resp_tipo_equipamento} | Isto está correto?")
        print("Digite 'S' para confimar e 'N' para reescrever.")
        print("")
        confirmacao_tipo_equipamento = input("").upper()
        print("")

        if confirmacao_tipo_equipamento == "S":
                break
        elif confirmacao_tipo_equipamento == "N":
                print("Insira o endereço novamente, abaixo:")
                print("")
                break
        else:
                print("")
                print("Valor inserido inválido.")
                print("")
    
    if confirmacao_tipo_equipamento == "S":
        break
#------------------------------------------------------------------------------------------------------------------------#


# INÍCIO PROGRAMAÇÃO DAS OBSERVAÇÕES DO EQUIPAMENTO
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Início da programação da inserção do tipo de equipamento do cliente. 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#Início do loop while para reinserção das observações
#-----------------------------------------------------------#
while True:
#-----------------------------------------------------------#

# Inserção das observações do equipamento
#-----------------------------------------------------------#
    print("Insira abaixo as observações do equipamento analisado.")
    print("")
    resp_observacao_equipamento = input("- ")
    print("")
#-----------------------------------------------------------#

# Início do loop while para reinserção da confirmação de escolha.
#-----------------------------------------------------------#
    while True:
#-----------------------------------------------------------#

# Confirmação das observações do equipamento
#-----------------------------------------------------------#
        print("A descrição das observações do equipamento está correta?")
        print("Digite 'S' para confimar e 'N' para reescrever.")
        print("")
        confirmacao_observacao_equipamento = input("").upper()
        print("")

        if confirmacao_observacao_equipamento == "S":
            break
        elif confirmacao_observacao_equipamento == "N":
            print("Insira o endereço novamente, abaixo:")
            print("")
            break
        else:
            print("")
            print("Valor inserido inválido.")
            print("")

    if confirmacao_observacao_equipamento == "S":
        break
#-----------------------------------------------------------#

# INÍCIO PROGRAMAÇÃO INSERÇÃO DE SENHA
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Início da programação da inserção da senha do equipamento do cliente. 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Início do loop while para inserção da senha de acesso
#-----------------------------------------------------------#
while True:
#-----------------------------------------------------------#

# Inserção de senha de acesso
#-----------------------------------------------------------#

    print ("O equipamento possui alguma senha de acesso?")
    print("Digite 'S' para confimar e 'N' para pular.")
    print("")
    confirmacao_senha_acesso = input("").upper()
    print("")
    
    if confirmacao_senha_acesso == "S":
        print("Insira a senha de acesso abaixo: ")
        print("")

        while True:     

            resp_senha_de_acesso = input("- ")
            print("")
            print (f"A senha inserida foi {resp_senha_de_acesso}| Isto está correto?")
            print("Digite 'S' para confimar e 'N' para reinserir.")
            print("")
            verificar_senha_acesso = input("- ").upper()
            print("")
            if verificar_senha_acesso == "S":
                break
            elif verificar_senha_acesso == "N":
                print("Insira a senha de acesso novamente.")
                print("")
            else:
                print("Valor inserido inválido. Coloque a senha novamente abaixo.")
                print("")
    
    elif confirmacao_senha_acesso == "N":
        confirmacao_senha_acesso = "O dispositivo não possui senha de acesso."
        break
    else: 
        print("Valor inserido inválido.")
        print("")

    if verificar_senha_acesso == "S":
        print("")
        break
#-----------------------------------------------------------#


# INÍCIO PROGRAMAÇÃO SERVIÇO SOLICITADO
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Início da programação da inserção do serviço solicitado para atendimento. 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Início do loop while para reinserção do serviço solicitado
#-----------------------------------------------------------#
while True:
#-----------------------------------------------------------#

# Inserção do serviço solicitado pelo cliente
#-----------------------------------------------------------#
    print("Insira abaixo o quê foi solicitado pelo cliente.")
    print("")
    resp_solicitado = input("- ")
    print("")
#-----------------------------------------------------------#

# Início do loop while para reinserção da confirmação de escolha.
#-----------------------------------------------------------#
    while True:
#-----------------------------------------------------------#

# Confirmação do serviço solicitado pelo cliente
#-----------------------------------------------------------#
        print("A descrição do serviço que foi solicitado pelo cliente está correta?")
        print("Digite 'S' para confimar e 'N' para reescrever.")
        print("")
        confirmacao_solicitado = input("").upper()
        print("")

        if confirmacao_solicitado == "S":
            break
        elif confirmacao_solicitado == "N":
            print("Insira o endereço novamente, abaixo:")
            print("")
            break
        else:
            print("")
            print("Valor inserido inválido.")
            print("")

    if confirmacao_solicitado == "S":
            break
#-----------------------------------------------------------#


# INÍCIO PROGRAMAÇÃO CONSTATADO EM VISITA
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Início da programação da inserção do o que foi constatado em visita.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Início do loop while para reinserção da constatação em visita
#-----------------------------------------------------------#
while True:
#-----------------------------------------------------------#


# Inserção do que foi constatado em visita
#-----------------------------------------------------------#
    print("Insira abaixo o quê foi constatado em visita:")
    print("")
    resp_constatado = input("- ")
    print("")
#-----------------------------------------------------------#

#Início do loop while para reinserção da confirmação de escolha.
#-----------------------------------------------------------#
    while True:
#-----------------------------------------------------------#

# Confirmação do serviço solicitado pelo cliente
#-----------------------------------------------------------#
        print("A descrição da constatação em visita durante o atendimento está correta?")
        print("Digite 'S' para confimar e 'N' para reescrever.")
        print("")
        confirmacao_constatado = input("").upper()
        print("")

        if confirmacao_constatado == "S":
            break
        elif confirmacao_constatado == "N":
            print("Insira o endereço novamente, abaixo:")
            print("")
            break
        else:
            print("")
            print("Valor inserido inválido.")
            print("")

    if confirmacao_constatado == "S":
            break
#-----------------------------------------------------------#

# INÍCIO PROGRAMAÇÃO IDENTIFICAÇÃO
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Início da programação da inserção da identificação do Técnico.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Início do loop while para reinserção do serviço solicitado
#-----------------------------------------------------------#
while True:
#-----------------------------------------------------------#

# Inserção do serviço solicitado pelo cliente
#-----------------------------------------------------------#
    print("Insira abaixo o nome do técnico que realizou o atendimento.")
    print("")
    resp_tecnico = input("- ")
    print("")
#-----------------------------------------------------------#

# Início do loop while para reinserção da confirmação de escolha.
#-----------------------------------------------------------#
    while True:
#-----------------------------------------------------------#

# Confirmação do serviço solicitado pelo cliente
#-----------------------------------------------------------#
        print("O nome do técnico está correto?")
        print("Digite 'S' para confimar e 'N' para reescrever.")
        print("")
        confirmacao_tecnico = input("").upper()
        print("")

        if confirmacao_tecnico == "S":
            break
        elif confirmacao_tecnico == "N":
            print("Insira o endereço novamente, abaixo:")
            print("")
            break
        else:
            print("")
            print("Valor inserido inválido.")
            print("")

    if confirmacao_tecnico == "S":
            break
#-----------------------------------------------------------#




# SALVAMENTO DE VALORES EM ARQUIVO
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Início da programação do salvamento dos valores inseridos em um arquivo separado.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Definição das pastas
#-----------------------------------------------------------#
pasta_raiz = "C:\\criador_os"
subpasta1 = os.path.join(pasta_raiz, "Arquivos_Salvos")
#-----------------------------------------------------------#

# Criando as pastas
#-----------------------------------------------------------#
os.makedirs(pasta_raiz, exist_ok=True)
os.makedirs(subpasta1, exist_ok=True)
#-----------------------------------------------------------#


print(f"Pastas criadas com sucesso: {pasta_raiz}, {subpasta1} | Consulte-as para acessar o arquivo salvo.")


# Inserção de local novo
#-----------------------------------------------------------#
local_novo = "C:\\OS_Creator\\Save_Data"
#-----------------------------------------------------------#

# Obter a data e hora atual no formato desejado
#-----------------------------------------------------------#
data_hora = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
#-----------------------------------------------------------#

# Criar o conteúdo do novo arquivo
#-----------------------------------------------------------#
conteudo_novo = f"""
Este é um documento salvo gerado pelo Criador de Ordens de Serviço.


-- Data de criação da OS: --

- {fim_ano} 

-----------------------------



-- Nome do cliente: --

- {resp_cliente}

------------------------



-- Endereço do cliente: --

- {resp_endereco}

---------------------------



-- Unidade Federativa: --

- {resp_uf}

--------------------------



-- Telefone: --

- {resp_telefone_str}

---------------



-- Tipo de atendimento: --

- {resp_tipo_atendimento}

----------------------------



-- Tipo de equipamento: --

- {resp_tipo_equipamento}

-----------------------------



-- Observações do equipamento: --

- {resp_observacao_equipamento}

--------------------------------------



-- Senha de acesso: --

- {resp_senha_de_acesso}

-----------------------



--Solicitado pelo cliente: --

- {resp_solicitado}

-----------------------------



-- Constatado em visita: --

- {resp_constatado}

----------------------------



-- Técnico responsável: --

- {resp_tecnico}

---------------------------
"""
#-----------------------------------------------------------#

# Gravar o conteúdo no novo local
#-----------------------------------------------------------#
with open(f"{subpasta1}\\nota_servico_{data_hora}.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo_novo)

print("Dados salvos com sucesso!")
print("")
print("Insira qualquer valor para sair do programa.")
input("")
#-----------------------------------------------------------#
