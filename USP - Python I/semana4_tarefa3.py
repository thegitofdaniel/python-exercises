n = input("Digite o valor de n: ")

digits = len(n)

counter = 0
valor = 0
soma = 0

while counter < digits:
	valor = int(n[counter])
	counter = counter + 1
	soma = soma + valor

print(soma)