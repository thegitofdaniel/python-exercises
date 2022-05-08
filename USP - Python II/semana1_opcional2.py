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