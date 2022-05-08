num = input("Digite o valor de n: ")

digits = len(num)

counter = 0
soma = 0
shortm = False
longm = False

while counter < (digits-1):
	valor1 = int(num[counter])
	counter = counter + 1
	valor2 = int(num[counter])

	if valor1 == valor2:
		shortm = True
	else:
		shortm = False
	longm = shortm or longm


if longm:
	print("sim")
else:
	print("não")