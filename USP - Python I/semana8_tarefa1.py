def remove_repetidos(lista):

	n = 0
	
	lista1 = lista[:]
	lista2 = lista[:]

	for i in lista1:

		del lista2[n]

		if i in lista2:
			lista1 = lista2[:]
		else:
			lista2 = lista1[:]
			n = n + 1
			pass
		
	return(sorted(lista2))
