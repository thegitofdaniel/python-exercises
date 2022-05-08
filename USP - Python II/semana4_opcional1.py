#gerador de números aleatórios interios num dado intervalo

def lista_grande(n,min=100000,max=100000):
	lista_grande = []
	i = 0
	while i < n:
		lista_grande.append(random.randint(-min,max))
		i = i + 1
	return(lista_grande)

#ordenar via comparação direta

def ordena(lista):
	for i in range((len(lista)-1)):

		posicao_do_minimo = i

		for j in range(i+1,len(lista)):

			if lista[j] < lista[posicao_do_minimo]:
				posicao_do_minimo = j

		lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo],lista[i]
	return(lista)