import registro
def ListarTodos(funcionarios):
    print("-"*50)
    for contrato in funcionarios:
        if contrato['funcao']!="DEMITIDO":
            print("-"*50)
            print(f"Nome: {contrato['nome']}\nIdade: {contrato['idade']}\nData da contratação: {contrato['data_contratado']}\n Contacto: {contrato['contacto']}\nCarta de condução: {contrato['carta_conducao']}\nFunção: {contrato['funcao']}")

def ListarFuncionario(funcionarios):
    encontrou=False
    nome_info=input("Insira o nome do funcionário a pesquisar:")
    for contrato in funcionarios:
        if contrato['funcao']!="DEMITIDO":
            if nome_info.lower()==contrato['nome'].lower():
                #verificar se encontrou algum nome
                encontrou=True
                print("-"*50)
                print(f"Nome: {contrato['nome']}\nIdade: {contrato['idade']}\nData da contratação: {contrato['data_contratado']}\nContacto: {contrato['contacto']}\nCarta de condução: {contrato['carta_conducao']}\nFunção: {contrato['funcao']}")
    if encontrou==False:
        print("-"*50)
        print("Funcionário não encontrado!")

def ListarDemitidos(funcionarios):
    print("-"*50)
    for contrato in funcionarios:
        if contrato['funcao']=="DEMITIDO":
            print("-"*50)
            print(f"Nome: {contrato['nome']}\nIdade: {contrato['idade']}\nData da contratação: {contrato['data_contratado']}\n Contacto: {contrato['contacto']}\nCarta de condução: {contrato['carta_conducao']}\nFunção: {contrato['funcao']}")

def EditarInfo(funcionarios):
    encontrou=False
    nome_info=input("Insira o nome do funcionário a pesquisar:")
    for contrato in funcionarios:
        if contrato['funcao']!="DEMITIDO":
            if nome_info.lower()==contrato['nome'].lower():
                #verificar se encontrou
                encontrou=True
                print("-"*50)
                print(f"Nome: {contrato['nome']}\nIdade: {contrato['idade']}\nData da contratação: {contrato['data_contratado']}\n Contacto: {contrato['contacto']}\nCarta de condução: {contrato['carta_conducao']}\nFunção: {contrato['funcao']}")
                op=input("Pretende editar as informações deste funcionário?[s/n]: ")
                if op=="s":
                    while True:
                        print("-"*50)
                        print("Qual parâmetro pretende editar?")
                        op=int(input("1.Nome\n2.Idade\n3.Contacto\n4.Carta de Condução:\n5.Função\n6.Terminar Edição\n:"))
                        if op==1:
                            novo_nome=input("Insira o novo nome: ")
                            contrato['nome']=novo_nome
                        elif op==2:
                            novo_idade=int(input("Atualize a idade:"))
                            contrato['idade']=novo_idade
                        elif op==3:
                            novo_contacto=int(input("Insira o novo contacto:"))
                            contrato['contacto']=novo_contacto
                        elif op==4:
                            novo_carta=input("Tem carta de condução?[s/n]")
                            if novo_carta=="s" or novo_carta=="n":
                                contrato['carta_conducao']=novo_carta
                            else:
                                print("Opção não válida")
                        elif op==5:
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
                                print("Opção não é válida\n")
                        else:
                            print("A terminar edição")
                            return
    if encontrou==False:
        print("-"*50)
        print("Funcionário não encontrado!")