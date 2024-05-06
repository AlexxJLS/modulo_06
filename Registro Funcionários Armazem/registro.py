import datetime

def Contratar(funcionarios):
    
    print("-"*50)
    print("---Novo contrato---")
    #pedir informações
    nome=input("Nome: ")
    while True:
        idade=int(input("Idade: "))
        if idade < 18:
            print("Não tem idade para trabalhar!")
            return
        if idade > 67:
            print("Não podemos contratar pessoas acima dos 67 anos!")
            return
        break
    
    data_contrato=datetime.datetime.now()
    #colocar a data organizada
    data_formatada=data_contrato.strftime("%d/%m/%Y")
    
    contacto=int(input("Contacto: "))

    while True:    
        #necessario para desempenhar a função de transportador
        carta_conducao=input("Tem carta de condução?(s/n): ")
        if carta_conducao=="s" or carta_conducao=="n":
            break
        print("Opção Inválida. Tente novamente!")
        

    #dicionario para guardar as informações
    contrato={
        "nome":nome,
        "idade":idade,
        "data_contratado":data_formatada,
        "contacto":contacto,
        "carta_conducao":carta_conducao,
        "funcao":""
    }

    while True:
        #pedir qual a função do funcionario
        op=int(input("\nDefina uma função no armazém:\n1.Transportador\n2.Vendedor\n3.Reposição de stock\n4.Encomenda para stock\n:"))
        if op==1:
            if contrato["carta_conducao"]=="n":
                print("O funcionário não tem carta de condução!")
                continue
            contrato["funcao"]="Transportador"
            break
        elif op==2:
            contrato["funcao"]="Vendedor"
            break
        elif op==3:
            contrato["funcao"]="Reposição de stock"
            break
        elif op==4:
            contrato["funcao"]="Encomenda para stock"
            break
        else:
            print("Opção não é válida. Tente novamente!\n")

    #adicionar o funcionário à lista de funcionários
    funcionarios.append(contrato)
    print(contrato)
    print("Funcionário contratado com sucesso!")

def demitir(funcionarios):
    encontrou=False
    nome_info=input("Insira o nome do funcionário a demitir:")
    for contrato in funcionarios:
        if nome_info.lower()==contrato['nome'].lower():
            encontrou=True
            print(f"Nome: {contrato['nome']}\nIdade: {contrato['idade']}\nData da contratação: {contrato['data_contratado']}\n Contacto: {contrato['contacto']}\nCarta de condução: {contrato['carta_conducao']}\nFunção: {contrato['funcao']}")
            op=input("Pretende demitir este contacto?[s/n]:")
            if op=="s":
                contrato['funcao']="DEMITIDO"
                print("-"*50)
                print(f"O funcionário {contrato['nome']} foi demitido com sucesso!")
    if encontrou==False:
        print("-"*50)
        print("Funcionário não encontrado!")        