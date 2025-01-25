import oracledb
import json

#funcoes
def marca_oficina(): #pergunta ao usuario se ele gostaria de marcar com alguma oficina
    
    while True:
        try:
            marcar_oficina=int(input("Você gostaria marcar uma com alguma oficina proxíma? (1)Sim ou (2)Não: \n-"))

            while marcar_oficina<1 or marcar_oficina>2:
                print("Opção Invalida!")
                marcar_oficina=int(input("Você gostaria marcar uma com alguma oficina proxíma? (1)Sim ou (2)Não: \n-"))
            
        except ValueError:
            print("Valor informado invalido. \nPor favor, tente novamente")
            
        else:
            break
    return marcar_oficina

def avaliar(): #pede a avaliaçao do usuario
    avaliacao=[]
    print("Avalie o programa!")
    
    while True:
        try:
            nota=int(input("Entre 0 e 10, o quanto você avalia nosso programa, sendo 0 muito ruim e 10 Muito bom: \n-"))
            while nota<0 or nota>10:  
                print("Opção invalida!")
                nota=int(input("Entre 0 e 10, o quanto você avalia nosso programa, sendo 0 muito ruim e 10 Muito bom: \n-"))
            avaliacao.append(nota)
            
        except ValueError:
            print("Valor informado invalido. \nPor favor, tente novamente")
            
        else:
            break
        
    print("Gostaria de deixar alguma sugestão para que possamos melhorar? Caso não queira, apenas pressione a tecla 'ENTER'")
    comentario=input("Comentário: ")
    if len(comentario) <=1:
        comentario="Não houve comentario"
    avaliacao.append(comentario)
    return avaliacao

def menu_principal(): 
    while True:    
        try: 
            primeira_selecao=int(input("Por favor, selecione uma das opções: \n(1)Problemas Com o Carro \n(2)Oficinas Próximas \n(3)Chamar Guincho \n(4)Cadastro na Porto \nOpção: "))
            
            while primeira_selecao<1 or primeira_selecao>4: 
                print("Seleção Invalida!")
                primeira_selecao=int(input("Por favor, selecione uma das opções novamente: \n(1)Problemas Com o Carro \n(2)Oficinas Próximas \n(3)Chamar Guincho \n(4)Cadastro na Porto \nOpção: "))
        
        except ValueError:
            print("Valor informado invalido. \nPor favor, tente novamente")
        
        else:
            break

    return primeira_selecao

def get_connection():
    connection = oracledb.connect('rm557957/300306@oracle.fiap.com.br:1521/orcl')
    return connection

def read():
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'SELECT * FROM CADASTRO'
    cursor.execute(sql)

    for linha in cursor:
        print(linha)

    connection.commit()
    cursor.close()
    connection.close()

def insert(nome,CPF,telefone,email,cidade,bairro,carro):
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'SELECT * FROM CADASTRO'
    cursor.execute(sql)

    sql = 'INSERT INTO CADASTRO (NOME, CPF, TELEFONE, EMAIL, CIDADE, BAIRRO, CARRO) VALUES (:1, :2, :3, :4, :5, :6, :7)'
    data = (nome, CPF, telefone, email, cidade, bairro, carro)
    cursor.execute(sql, data)

    connection.commit()
    cursor.close()
    connection.close()

def delete(cpf):
    connection= get_connection()
    cursor = connection.cursor()
    sql = 'SELECT * FROM CADASTRO'
    cursor.execute(sql)

    colunas = cursor.fetchall()
    if not colunas:
        print("Não existem dados cadastrados.")
    
    else:
        sql = "DELETE FROM CADASTRO WHERE CPF = :cpf"

        cursor.execute(sql, {"cpf": cpf})

    connection.commit()
    cursor.close()
    connection.close()

def update(CPF, coluna, novo_valor):
    connection = get_connection()
    cursor= connection.cursor()

    sql = f"UPDATE cadastro SET {coluna} = :novo_valor WHERE cpf = :cpf"
    
    # Execute a consulta com os parâmetros
    cursor.execute(sql, {"novo_valor": novo_valor, "cpf": CPF})

    connection.commit()
    cursor.close()
    connection.close()

def cadastro(): #realiza o cadastro do cliente
    nome=input("Certo. Por favor, informe o seu nome: ")
    CPF=input("CPF: ")
    telefone=input("Telefone com DDD: ")
    email=input("Email: ")
    cidade_cliente=input("Cidade: ")
    bairro_cliente=input("Bairro: ")
    carro=input("Informe o modelo do seu carro: ")
    
    print(f"Certo. Confira seus dados: \nnome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente} \nModelo: {carro}")
    while True:    
        try:   
            confirmar_cadastro=int(input("Confirmar dados? (1)Sim ou (2)Não: \n-"))

            while confirmar_cadastro>2 or confirmar_cadastro<1:
                print("Esta opção não existe!")
                confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente} \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-"))

        except ValueError:
            print("Valor informado invalido. \nPor favor, tente novamente")
        
        else:
            break
        
    while confirmar_cadastro == 2:
                print("Tudo bem, qual informação você gostaria de alterar?")
                refazer_cadastro=int(input("(1)Nome \n(2)CPF \n(3)Telefone \n(4)Email \n(5)Cidade \n(6)Bairro \n(7)Modelo: \n-"))
                match refazer_cadastro:
                    case 1: #nome
                        nome=input("Informe o seu nome novamente: ")
                        confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente}  \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-"))

                        while confirmar_cadastro>2 or confirmar_cadastro<1:
                            print("Esta opção não existe!")
                            confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente}  \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-"))
                    
                    case 2: #cpf
                        CPF=int(input("Informe o seu CPF novamente: "))
                        confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente}  \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-"))

                        while confirmar_cadastro>2 or confirmar_cadastro<1:
                            print("Esta opção não existe!")
                            confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente}  \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-"))
                    
                    case 3: #telefone
                        telefone=int(input("Informe o seu telefone com DDD novamente: "))
                        confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente}  \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-"))

                        while confirmar_cadastro>2 or confirmar_cadastro<1:
                            print("Esta opção não existe!")
                            confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente}  \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-"))
                    
                    case 4: #email
                        email=input("Informe o seu Email novamente: ")
                        confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente}  \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-"))

                        while confirmar_cadastro>2 or confirmar_cadastro<1:
                            print("Esta opção não existe!")
                            confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente}  \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-"))
                    
                    case 5: #cidade
                        cidade_cliente=input("Informe sua cidade novamente: ")
                        confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente}  \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-"))

                        while confirmar_cadastro>2 or confirmar_cadastro<1:
                            print("Esta opção não existe!")
                            confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente}  \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-")) 
                
                    case 6: #bairro
                        bairro_cliente=input("Informe o seu bairro novamente: ")
                        confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente}  \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-"))

                        while confirmar_cadastro>2 or confirmar_cadastro<1:
                            print("Esta opção não existe!")
                            confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente}  \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-"))

                    case 7:
                        carro=input("informe o modelo do seu carro") 
                        confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente}  \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-"))

                        while confirmar_cadastro>2 or confirmar_cadastro<1:
                            print("Esta opção não existe!")
                            confirmar_cadastro=int(input(f"Nome: {nome} \nCPF: {CPF} \nTelefone: {telefone} \nEmail: {email} \nCidade: {cidade_cliente} \nBairro: {bairro_cliente}  \nModelo: {carro} \nConfirmar dados? (1)Sim ou (2)Não: \n-"))
    insert(nome,CPF,telefone,email,cidade_cliente,bairro_cliente,carro)
    print("Cadastro realizado com sucesso!")
    return CPF

def compactar_json():
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'SELECT * FROM CADASTRO'
    cursor.execute(sql)

    # Pega o nome das colunas
    colunas = [desc[0] for desc in cursor.description]
    
    # Busca todas as linhas
    rows = cursor.fetchall()
    if not rows:
        print("Não existem dados cadastrados.")
        data = []  # Lista vazia para o JSON
    else:
        # Converte cada linha em um dicionário com os nomes das colunas
        data = [dict(zip(colunas, row)) for row in rows]

    cursor.close()
    connection.close()
    
    # Escreve os dados em um arquivo JSON
    with open("cadastro.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Dados exportados para cadastro.json")
#main

x=1 #variavel de controle

print("Bem vindo(a) ao programa de auto diagnóstico da Porto Seguro!")
while x == 1:
    problema=0
    marcar_oficina=0

    primeira_selecao=menu_principal()
    
    match primeira_selecao:
        case 1: #problema no carro
            print("Opção selecionada: Problemas Com o Carro")
            while True:    
                try:   
                    print("Opção selecionada: Problemas Com o Carro")
                    problema=int(input("Por favor, selecione o problema que o seu carro pode estar aprensentando: \n(1)Alinhamento \n(2)Ar Condicionado \n(3)Arrefecimento \n(4)Balanceamento e Geometria \n(5)Correias \n(6)Discos e Pastilhas de Freio \n(7)Embreagem \n(8)Filtros e Velas de Ignição \n(9)Outro \nOpção: "))
                    while problema <1 or problema>9: 
                        print("Seleção Invalida!")
                        problema=int(input("Por favor, selecione novamente o problema que o seu carro pode estar aprensentando de 1 a 8: \n(1)Alinhamento \n(2)Ar Condicionado \n(3)Arrefecimento \n(4)Balanceamento e Geometria \n(5)Correias \n(6)Discos e Pastilhas de Freio \n(7)Embreagem \n(8)Filtros e Velas de Ignição \n(9)Outro \nOpção: "))

                except ValueError:
                    print("Valor informado invalido. \nPor favor, tente novamente")
        
                else:
                    break
           
            if problema >=1 or problema<=8:
                descricao_problema=input("Certo, agora descreva o problema com o MAXÍMO de detalhes possíveis. \n-")
                
        case 2: #oficinas proximas
            print("Opção selecionada: Oficinas Próximas")
            cidade=input("Por favor, informe a sua cidade: \n-")
            bairro=input("Agora, informe o seu bairro: \n-")
            print("Existem X oficinas proxímas de você")

        case 3:#chamar guincho
            print("Opção selecionada: Chamar Guincho")
            cidade_guincho=input("Por favor, informe a cidade \n-")
            bairro_guincho=input("Por favor, informe o bairro \n-")
            endereço=input("Por favor, informe o endereço do local \n-")
            print("Certo, existem X guinchos próximos de você e um já está a caminho!")

        case 4: #cadastro na porto
            print("Opção selecionada: Cadastro na Porto")
            menu_crud = 0
            while True:
                try:
                   
                    menu_crud= int(input("Selecione uma opção: \n1- Fazer cadastro \n2- Ver cadastro \n3- Alterar cadastro \n4- Deletar cadastro \n5- Sair \n- "))
                    while menu_crud >5 or menu_crud <1:
                        menu_crud= int(input("Opcão invalida. Por favor selecione uma opção: \n1- Fazer cadastro \n2- Consultar cadastro \n3- Alterar cadastro \n4- Deletar cadastro \n5- Sair\n- "))

                    match menu_crud:
                        case 1:
                            cadastro_cliente=cadastro()

                        case 2:
                            read()
                            try:
                                compactarjson = int(input("Voce deseja salvar essas informaçoes? \n1- Sim \n2- Não \n-"))
                                while compactarjson <1 or compactarjson> 2:
                                    compactarjson = int(input("Opção invalida! Voce deseja salvar essas informaçoes? \n1- Sim \n2- Não"))
                            
                            except ValueError:
                                print("Valor Informado Invalido")
                            
                            else:
                                match compactarjson:
                                    case 1: compactar_json()
                                
                                    case 2: 
                                        print("Certo")
                            
                            finally:
                                print("Saindo...")

                        case 3:
                            try:   
                                CPF = input("Informe o seu CPF: ")

                                coluna = input("Qual coluna deseja alterar? \n  Nome \n CPF \n Telefone \n Email \n Cidade \n Bairro \n Carro\n -")
                            
                                novo_valor= input("Novo dado: ")
                            
                            except ValueError:
                                print("Valor informado invalido. \nPor favor, tente novamente")

                            else:
                                update(CPF, coluna, novo_valor)
                        
                        case 4:
                            cpf = input("Informe o CPF: ")
                            delete(cpf)
                        
                        case 5:
                            print("Saindo...")
            
                except ValueError:
                    print("Valor informado invalido. \nPor favor, tente novamente")
            
                else:
                    print("Operações bem sucedidas!")
                    break

    match problema:
        case 1: #alinhamento
            print("Certo. Problemas com o alinhamento costumam ter uma média de valor de R$000.00, podendo variar o valor de acordo com o lugar e gravidade do problema.")
            marcar_oficina=marca_oficina()
                    
        case 2: #ar condicionado
            print("Certo. Problemas com o ar condicionado costumam ter uma média de valor de R$000.00, podendo variar o valor de acordo com o lugar e gravidade do problema.")
            marcar_oficina=marca_oficina()
                
        case 3: #arrefecimento
            print("Certo. Problemas com arrefecimento costumam ter uma média de valor de R$000.00, podendo variar o valor de acordo com o lugar e gravidade do problema.")
            marcar_oficina=marca_oficina()
                
        case 4: #balanceamento e geometria
            print("Certo. Problemas com o balanceamento e geometria costumam ter uma média de valor de R$000.00, podendo variar o valor de acordo com o lugar e gravidade do problema.")
            marcar_oficina=marca_oficina()

        case 5: #correias
            print("Certo. Problemas com as correias costumam ter uma média de valor de R$000.00, podendo variar o valor de acordo com o lugar e gravidade do problema.")
            marcar_oficina=marca_oficina()
                
        case 6: #discos e pastilhas de freio
            print("Certo. Problemas com os discos e pastilhas de freio costumam ter uma média de valor de R$000.00, podendo variar o valor de acordo com o lugar e gravidade do problema.")
            marcar_oficina=marca_oficina()

        case 7: #embreagem
            print("Certo. Problemas com a embreagem costumam ter uma média de valor de R$000.00, podendo variar o valor de acordo com o lugar e gravidade do problema.")
            marcar_oficina=marca_oficina()

        case 8: #filtros e velas e igniçao
            print("Certo. Problemas com os filtros e velas de igniçãoo costumam ter uma média de valor de R$000.00, podendo variar o valor de acordo com o lugar e gravidade do problema.")
            marcar_oficina=marca_oficina()

        case 9: #outro
            possivel_problema=input("Certo. Por favor, informe onde poderia ser o problema: \n-")
            marcar_oficina=marca_oficina()
        
    match marcar_oficina:
        case 1: #quer marcar oficina / caso nao queira o programa é encerrado
            print("Certo")
            possui_cadastro=int(input("Você possui cadastro na Porto Seguro? (1)Sim ou (2)Não: \n-"))

            while possui_cadastro<1 or possui_cadastro>2:
                print("Opção invalida!")
                possui_cadastro=int(input("Você possui cadastro na Porto Seguro? (1)Sim ou (2)Não: \n-"))

            match possui_cadastro:
                case 1: #tem cadastro
                    informar_cpf=int(input("Por favor, infome o seu CPF: \n-")) #se o CPF for invalido vai retornar uma mensagem dizendo "CPF invalido" e vai pedir para inserir novamente
                    confirmar_cidade=int(input("Esta é a sua cidade? (cidade do cadastro do cliente) (1)Sim ou (2)Não: "))

                    while confirmar_cidade<1 or confirmar_cidade>2:
                        print("Opção Invalida!")
                        confirmar_cidade=int(input("Esta é a sua cidade? (cidade do cadastro do cliente) (1)Sim ou (2)Não: "))
                    
                    if confirmar_cidade==2:
                        cidade_cliente=input("Por favor, informe a sua cidade: ")
                    
                    confirmar_bairro=int(input("Este é o seu bairro? (bairro do cadastro do cliente) (1)Sim ou (2)Não: "))
                    
                    while confirmar_bairro<1 or confirmar_bairro>2:
                        print("Opção Invalida!")
                        confirmar_bairro=int(input("Este é o seu bairro? (bairro do cadastro do cliente) (1)Sim ou (2)Não: "))
                    
                    if confirmar_bairro==2:
                        bairro_cliente=input("Por favor, informe o seu bairro: ")
                    
                    print("Tudo Certo!")
                    print("Existe uma oficina próxima de você com disponibilidade para o dia: (dia)")
                    
                case 2: #nao tem cadastro
                    fazer_cadastro=int(input("Gostaria de fazer? (1)Sim ou (2)Não: \n-"))

                    while fazer_cadastro<1 or fazer_cadastro>2:
                        print("Opção Invalida!")
                        fazer_cadastro=int(input("Gostaria de fazer? (1)Sim ou (2)Não: \n-"))
                    
                    if fazer_cadastro==1: 
                        cadastro_cliente=cadastro()

                    print("Tudo Certo")
                    print("Existe uma oficina próxima de você com disponibilidade para o dia: (dia)") #(dia)= dia disponivel da oficina

    
    x=int(input("Você gostaria de retornar ao menu principal? (1)Sim ou (2)Não: \n-"))
    while x<1 or x>2:
        print("Opção invalida! ")
        x=int(input("Você gostaria de retornar ao menu principal? (1)Sim ou (2)Não: \n-"))

    if x == 1:
        print("Retornando ao menu principal")
    else:
        print("Encerrando o sistema")

#avaliação do serviço
avaliacao=avaliar()

#finalizaçao
print("Obrigado por usar o programa!")




    
   

    

