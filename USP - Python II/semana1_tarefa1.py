def dimensoes(minha_matriz):

	linha = len(minha_matriz)
	if type(minha_matriz[0]) == list:
		coluna = len(minha_matriz[0])
	else:
		coluna = 1

	print(str(linha)+"X"+str(coluna))