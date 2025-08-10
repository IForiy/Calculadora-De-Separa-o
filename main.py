import pandas as pd

banco = pd.read_csv("dados.csv", sep=";")  
contador=0
dadosValidos = banco.dropna(how='all')
qntdLinha = len(dadosValidos)
codSaco = banco.loc[contador, "codSaco"]

pesoEmbalgemSaco = 0.02
verificaRes = False

while verificaRes == False:
    perguntacodSaco = input("Qual é o codigo do saco? ")

    while  contador < qntdLinha:
        codSaco = banco.loc[contador, "codSaco"]
    
        if perguntacodSaco == codSaco:

            print(codSaco)
            pesoFardo = banco.loc[contador, "pesoFardo"]
            print(pesoFardo)
            qntdFardo = banco.loc[contador,"qntdFardo"]
            qntdSeparacao = int(input("Qual a quantidade que voce precisa separar? "))
            peso_da_qtnd_do_saco = ((qntdSeparacao*pesoFardo/qntdFardo)+pesoEmbalgemSaco)*1.03
            print(f"Peso de separacao e {peso_da_qtnd_do_saco:.2f} do saco {codSaco}")
            contador = qntdLinha
            verificaRes = True
            
        else:
            contador += 1

    if verificaRes == False:
        print("Esse codigo de SACO NAO EXISTE, tente outro CODIGO")
        contador= 0   












