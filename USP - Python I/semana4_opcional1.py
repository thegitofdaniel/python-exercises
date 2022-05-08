x = int(input("Digite um número inteiro: "))

counter = x - 1

while counter > 1:
	resto = x % counter
	if resto == 0:
		print("não primo")
		break
	elif counter > 2:
		counter = counter - 1
	else:
		print("primo")
		break

