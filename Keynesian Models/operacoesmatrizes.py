def imprime_matriz(minha_matriz):
	for i in minha_matriz:
		for j in i:
			print(j, end = " ") if (i.index(j) < len(minha_matriz[0]) - 1) else print(j, end ="")
		print()

def dimensoes(minha_matriz):

	linha = len(minha_matriz)
	if type(minha_matriz[0]) == list:
		coluna = len(minha_matriz[0])
	else:
		coluna = 1

	return(linha,coluna)

def sao_multiplicaveis(m1,m2):
	dim1 = dimensoes(m1)
	dim2 = dimensoes(m2)

	if dim1[1]==dim2[0]:
		#print("sao_multiplicaveis(m1, m2) =>", True)
		return True
	else:
		#print("sao_multiplicaveis(m1, m2) =>",False)
		return False

def soma_matrizes(m1,m2):

	dim1 = dimensoes(m1)
	dim2 = dimensoes(m2)

	matriz_soma = []
	
	if dim1 == dim2:

		if type(m1[0]) == list:

			for i in range(len(m1)):

				linha = []

				for j in range(len(m1[i])):
					linha.append(m1[i][j] + m2[i][j])
				matriz_soma.append(linha)

		else:

			for i in range(len(m1)):
				matriz_soma.append(m1[i] + m2[i])


		#print("soma_matrizes(m1, m2) =>",matriz_soma)
		return matriz_soma

	else:
		#print("soma_matrizes(m1, m2) => False")
		return 

def determinante2x2(matriz):
	assert len(matriz) == len(matriz[0])

	determinante = matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0]

	return(determinante)

def multmatrizes(m1,m2):

	lin1=len(m1)
	col1=len(m1[0])

	lin2=len(m2)
	col2=len(m2[0])

	linhas_prod = len(m1)
	colunas_prod = len(m2[0])

	assert col1 == lin2

	matriz_produto = []

	for i in range(lin1):

		matriz_produto.append([])

		for j in range(col2):

			matriz_produto[i].append(0)

			for k in range(col1):

				matriz_produto[i][j] += m1[i][k] * m2[k][j]

	return(matriz_produto)

def multescalar(m1,k):
	for i in range(len(m1)):
		for j in range(len(m1[0])):
			m1[i][j] = k*m1[i][j]
	return(m1)