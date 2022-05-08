#lista ordenada -> a lista está ordenada?

def ordenada(lista):
	ordenada = sorted(lista)

	return True if ordenada == lista else False

#busca sequencial -> onde está o elemento buscado?

def busca(lista,elemento):
	for i in range(len(lista)):
		if lista[i] == elemento:
			return i
	return False

import random