largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

i=1
j=1

while j <= altura:
	if ((j == 1) or (j == altura)):
		while i <= largura:
			print("#", end="")
			i = i + 1
	else:
		while i <= largura:
			print("#" if (i == 1 or i == largura) else " ", end="" )
			i = i + 1
	print()
	i = 1
	j = j+1
