
#def mult_matriz(x,y):
#	assert (len(x) > 0) and (len(x[0]) > 0)
#	assert (len(y) > 0) and (len(y[0]) > 0)
#	assert len(x) == len(y[0])


def cofator(matriz,i,j):

	cofator = matriz[:i]+ matriz[i+1:] #cofator que corta a iesima linha de x

	for linha in range(len(cofator)):

		cofator[linha] = cofator[linha][:j]+ cofator[linha][j+1:]

	return cofator

def achazeros_linha (matriz):
	maxzeros = 0
	linhazeros = 0

	for i in range(len(matriz)):
		aux= 0
		for j in matriz[i]:
			if j == 0:
				aux +=1
		if aux > maxzeros:
			maxzeros = aux
			linhazeros = i

	return(linhazeros)

# ----> TESTES de cofatores calculados manualmente
#print(cofator([[8,7],[9,2]],0,0))
#print(cofator([[8,3,7],[9,5,2],[2,1,4]],0,0))


def determinante(matriz, i=0):

	assert len(matriz) == len(matriz[i])

	i = achazeros_linha(matriz)

	d = 0

	if len(matriz) == 1: #base da recursao

		return matriz[i][0]

	else:

		for j in range(len(matriz[i])):

			if matriz[i][j] != 0:

				d = d + matriz[i][j]*(-1)**(i+j)*determinante(cofator(matriz,i,j))

	return d

# ----> TESTES de determinantes calculados manualmente
#print(determinante([[8]]))
#print(determinante([[8,7],[9,2]]))
#print(determinante([[8,3,7],[9,5,2],[2,1,4]]))
#print(determinante([[2,5,6],[1,6,7],[-1,2,3]]))
#import time
#x = time.time()
#print(determinante([[2,1,3,2],[2,0,0,4],[1,5,2,3],[2,1,4,6]]),)
#print(time.time() - x)
#print(determinante([[2,1,3,6,2],[2,0,0,4,4],[1,5,2,3,3],[2,2,1,4,6],[2,3,1,2,7]]))