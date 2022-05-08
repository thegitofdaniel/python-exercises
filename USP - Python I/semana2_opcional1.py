nome = input("Digite o nome do cliente: ")
dia_venc = input("Digite o dia de vencimento: ")
mes_venc = input("Digite o mês de vencimento: ")
fatura = "R$ " + input("Digite o valor da fatura: ")

data = dia_venc + " de " + mes_venc

print("Olá,",nome)
print("A sua fatura com vencimento em",data,"no valor de",fatura,"está fechada.")
