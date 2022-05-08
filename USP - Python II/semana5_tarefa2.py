def bubble_sort(lista):

	trocado = True

	while trocado:

		trocado = False

		for i in (range(len(lista)-1)):

			if lista[i] > lista[i+1]:

				lista[i], lista[i+1] = lista[i+1], lista[i]
				trocado = True

		print(lista)

	return lista

