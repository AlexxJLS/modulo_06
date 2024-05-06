"""Fazer a validação dos (),[] e {}
"""
import sys

argv=sys.argv
if len(argv)==1:
    expressao=input("Expressão a validar:")
else:
    expressao=argv[1]

#pares
pares={
    '(':')',
    '[':']',
    '{':'}'
}
#para guardar os ( [ { a abrir
stack=[]
#flag para indicar estado da expressao
correto=True

#percorrer a expressão
for c in expressao:
    print(c)
    #verificar se é um ( [ {
    if c in pares.keys():
        stack.append(c)
    elif c in pares.values():
        #verificar se tem um ( [ { 
        if len(stack)==0:
            print(f"Erro na expressão em {c}")
            correto=False
            break
        else:
            t=stack.pop()
            if pares[t]!=c:
                print(f"Erro na expressão em {c}")
                correto=False
                break

#ficou algum ( [ { por fechar
if len(stack)!=0:
    print("Erro na expressão!Expressão incompleta")

if correto==True:
    print("Expressão correta")