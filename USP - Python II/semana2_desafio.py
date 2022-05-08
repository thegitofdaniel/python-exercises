def multiplicar_matrizes(m1,m2):

	linhas_prod = len(m1)
	colunas_prod = len(m1[0])

	assert len(m1) == len(m2[0])

	matriz_produto = []

	for i in range(linhas_prod):

		matriz_produto.append([])

		for j in range(colunas_prod):

			matriz_produto[i].append(0)

			for k in range(linhas_prod):

				matriz_produto[i][j] += m1[i][k] * m2[k][j]

	return(matriz_produto)

def determinante2x2(matriz):
	assert len(matriz) == len(matriz[0])

	determinante = matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0]

	return(determinante)