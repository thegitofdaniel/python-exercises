def menor_nome(nomes):

	min = len(nomes[0].replace(" ",""))
	menor_nome = nomes[0].replace(" ","")

	for i in nomes:
		aux = len(i.replace(" ",""))
		if aux < min:
			min = aux
			menor_nome = i.replace(" ","")
		else:
			pass
	return(menor_nome.capitalize())