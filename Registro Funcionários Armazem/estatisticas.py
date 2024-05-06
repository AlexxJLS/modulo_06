def Estatisticas(funcionarios):
    #se eu usar len(funcionarios) irá contar também os demitidos
    nr_funcionarios=0
    
    soma_idades=0
    
    transportador=0
    vendedor=0
    repor_stock=0
    encomenda_stock=0
    
    carta=0

    for contrato in funcionarios:
        #ver apenas os que não foram demitidos
        if contrato['funcao']!="DEMITIDO":
            #contar o nº de funcionários
            nr_funcionarios+=1
            #somar idades
            soma_idades+=contrato['idade']
            
            #calcular nº de funcionários em cada função
            if contrato['funcao']=="Transportador":
                transportador+=1
            elif contrato['funcao']=="Vendedor":
                vendedor+=1
            elif contrato['funcao']=="Reposição de stock":
                repor_stock+=1
            else:
                encomenda_stock+=1

            #calcular nº de funcionários com carta de condução
            if contrato['carta_conducao']=="s":
                carta+=1
    #ver se existem funcionários
    if nr_funcionarios==0:
        print("-"*50)
        print("Impossível fazer estatísticas, não existem funcionários!")    
        return
    #calcular media de idades    
    media_idades=soma_idades/nr_funcionarios

    #calcular percentagem de funcionários
    def PerFuncao(funcao,nr_funcionarios):
        per_funcao=(funcao/nr_funcionarios)*100
        return per_funcao
    #guardar a percentagem de funcionários numa função
    per_transportador=PerFuncao(transportador,nr_funcionarios)    
    per_vendedor=PerFuncao(vendedor,nr_funcionarios)
    per_repor_stock=PerFuncao(repor_stock,nr_funcionarios)
    per_encomenda_stock=PerFuncao(encomenda_stock,nr_funcionarios)
    #guardar a percentagem de funcionários com carta de condução
    per_carta=PerFuncao(carta,nr_funcionarios)

    print("-"*50)
    print(f"Existem {nr_funcionarios} funcionários neste armazém. A média de idades dos funcionários é {media_idades} anos.")
    print("-"*50)
    print(f"Media de funcionários por funções:\nTransportador:{per_transportador}%\nVendedor:{per_vendedor}%\nReposição de Stock:{per_repor_stock}%\nEncomenda de Stock:{per_encomenda_stock}%")
    print("-"*50)
    print(f"{carta} funcionários teem carta de condução, que equivale a {per_carta}% dos funcionários")