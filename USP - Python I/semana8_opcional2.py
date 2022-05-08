x = 1
lista = []

while x != 0:
	x = int(input("Digite um número: "))
	lista.append(x)

del lista[-1]

for i in range(len(lista)):
	print(lista[-i-1])

#espelho = []

#for i in range(len(lista)):
#	espelho.append(lista[-i-1])

#for i in espelho:
#	print(i)
