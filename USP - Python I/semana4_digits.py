numstr = input("Digite aqui o número: ")
numint = len(numstr)

digits = 0
sumdigits = 0

while digits <= (numint-1):
    value = int(numstr[digits])
    #print(value)
    sumdigits = sumdigits + value
    digits = digits + 1

print(sumdigits)