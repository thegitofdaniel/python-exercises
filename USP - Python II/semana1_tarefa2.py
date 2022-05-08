def dimensoes(minha_matriz):

	linha = len(minha_matriz)
	if type(minha_matriz[0]) == list:
		coluna = len(minha_matriz[0])
	else:
		coluna = 1

	return(linha,coluna)

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
		return False