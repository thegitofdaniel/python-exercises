def maiusculas(frase):
	aux = ""
	for i in frase:
		if ord(i) >= 65 and ord(i) <= 90:
			aux += i
		else:
			pass
	return(aux)