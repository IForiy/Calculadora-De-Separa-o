
codSaco = "205.0015"
peso_fardo_Saco = 7.136
qntd_de_saco_por_fardo = 500
peso_do_saco_para_guardar_embalgem = 0.02



qntd_de_saco_para_separar = int(input("Qual a quantidade que voce precisa separar? "))


peso_da_qtnd_do_saco = ((qntd_de_saco_para_separar*peso_fardo_Saco/qntd_de_saco_por_fardo)+peso_do_saco_para_guardar_embalgem)*1.03

print(f"O peso de {qntd_de_saco_para_separar} é {peso_da_qtnd_do_saco:.2f}")





