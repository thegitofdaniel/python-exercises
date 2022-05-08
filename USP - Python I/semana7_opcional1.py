def n_primos(principal):
	aux = principal - 1
	contador_primos = 0
	naoPrimo = False
	
	while principal >2:
		while aux >= 2:
			naoPrimo = ((principal % aux) == 0)
			aux = aux - 1
			if naoPrimo:
				break
			else:
				if aux == 1:
					contador_primos = contador_primos+1
				else:
					pass
				continue

		principal = principal - 1
		aux = principal - 1

	print(contador_primos+1)