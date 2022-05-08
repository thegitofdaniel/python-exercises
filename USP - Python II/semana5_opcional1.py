def insertion_sort(lista):

	for index in range(1,len(lista)):

		elemento = lista[index]

		posicao = index

		while posicao > 0 and lista[posicao-1] > elemento:

			lista[posicao] = lista[posicao-1]

			posicao = posicao-1

		lista[posicao] = elemento

	return lista

#lista = [54,26,93,17,77,31,44,55,20]
#insertion_sort(lista)
#print(lista)