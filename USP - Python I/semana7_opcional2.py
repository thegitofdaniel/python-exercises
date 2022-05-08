def é_hipotenusa(x):
	hipotenusa = False
	catetoA = 1
	catetoB = 1

	while catetoA <= x:
		while catetoB <= x:
			hipotenusa = (hipotenusa or (x**2 ==(catetoA**2 + catetoB**2)))
			catetoB = catetoB + 1
		catetoB = 1
		catetoA = catetoA + 1
	return hipotenusa

def soma_hipotenusas(n):
	counter = 1
	soma = 0
	while counter <= n:
		if é_hipotenusa(counter):
			soma = soma + counter
		else:
			pass
		counter = counter + 1
	print(soma)

soma_hipotenusas(25)