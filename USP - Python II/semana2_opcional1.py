def conta_letras(frase, contar="vogais"):

	frase = frase.lower().replace(" ","")

	total = len(frase)

	for i in frase:
		frase = frase.replace("a","")
		frase = frase.replace("e","")
		frase = frase.replace("i","")
		frase = frase.replace("o","")
		frase = frase.replace("u","")
		consoantes = len(frase)

	if contar == "vogais":
		return(total - consoantes)

	else:
		return(consoantes)