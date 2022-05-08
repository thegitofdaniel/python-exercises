def imprime_matriz(minha_matriz):
	for i in minha_matriz:
		for j in i:
			print(j, end = " ") if (i.index(j) < len(minha_matriz[0]) - 1) else print(j, end ="")
		print()