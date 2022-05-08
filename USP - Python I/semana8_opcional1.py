def maior_elemento(lista):
	movel=lista[0]
	for i in lista:
		if i > movel:
			movel = i
		else:
			pass
	return(movel)
