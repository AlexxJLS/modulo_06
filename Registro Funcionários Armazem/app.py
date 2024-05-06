import registro
import info
import estatisticas

DEBUG=True

def main():
    print("="*50)
    print("Bem Vindo!")

    #versao para testes
    if DEBUG:
        funcionarios=[
            {'nome': 'Alex', 'idade': 18, 'data_contratado': '24/04/2024', 'contacto': 931970987, 'carta_conducao': 'n', 'funcao': 'Transportador'},
            {'nome': 'Afonso', 'idade': 42, 'data_contratado': '22/04/2024', 'contacto': 931854029, 'carta_conducao': 'n', 'funcao': 'Reposição de stock'},
            {'nome': 'Brito', 'idade': 34, 'data_contratado': '13/02/2022', 'contacto': 931854854, 'carta_conducao': 's', 'funcao': 'Encomenda para stock'},
            {'nome': 'Markes', 'idade': 22, 'data_contratado': '22/01/2018', 'contacto': 935324029, 'carta_conducao': 's', 'funcao': 'Vendedor'}
        ]
    else:
        #lista para guardar os funcionários
        funcionarios=[]

    def menu():
        print("="*50)
        print("Menu:\n1.Contratar\n2.Ver Informações\n3.Editar Informações\n4.Demitir\n5.Ver estatísticas\n6.Sair")

    while True:
        menu()
        print("-"*50)
        op=int(input("Insira a opção: "))
        if op==1:
            registro.Contratar(funcionarios)
        elif op==2:
            opcao=int(input("1.Listar Todos\n2.Procurar pelo nome\n3.Listar demitidos\n:"))
            if opcao==1:
                info.ListarTodos(funcionarios)
            elif opcao==2:
                info.ListarFuncionario(funcionarios)
            elif opcao==3:
                info.ListarDemitidos(funcionarios)
            else:
                print("Opção não é valida!")
                
        elif op==3:
            info.EditarInfo(funcionarios)
        elif op==4:
            registro.demitir(funcionarios)
        elif op==5:
            estatisticas.Estatisticas(funcionarios)
        elif op==6:
            print("A encerrar programa...")
            break
        else:
            print("A opção não é válida. Tente novamente!")

if __name__=="__main__":
    main()