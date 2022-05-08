# Classe ----------------------------------------

#class Lista:
#  def append(self, elemento):
#    return "Oops! Este objeto não é uma lista"
    
#lista = []

#a = Lista()
#b = a.append(7)

#lista.append(b)


#def calculo(x, y = 10, z = 5):
#    return x + y * z;
#calculo()

# Objetos ----------------------------------------

#lista1 = ["carro", "ônibus", "barco", "bicicleta"]
#lista2 = ["carro", "ônibus", "barco", "bicicleta"]
#lista3 = ["carro", "barco"]

#question = (lista3 is lista2)

#print(question)

# Condições ----------------------------------------

#Pass = True
#while Pass:
#	print("TruePasses")

#Pass = False
#while Pass:
#	print("FalsePasses")

#def study_loop():
#	x = 1
#	while x !=0:
#		x = int(input("digite x: "))
#	print("x é igual a 0")

# Laços ----------------------------------------

#def desenha(linha):    
#    while linha > 0:
#        coluna = 1
#        while coluna <= linha:
#            print('*', end = "")
#            coluna = coluna + 1
#        print()
#        linha = linha - 1

#desenha(5)

#i=1
#x = 2
#cont = 0
#while x >= 0:
#    y = 0
#    while y >= 4:
#        print(i)
#        i = i+1
#        y = y + 1
#    x = x - 1

# Retorno de funções ----------------------------------------

#def change(x,y):
#	aux = x
#	x = y
#	y = aux
#	return (x,y)

#x = 10
#y = 20

#(x,y) = change(x,y)

#print("x =", x,"e y =",y)

# Funções ----------------------------------------

#def soma(num1, num2, num3):
#    return num1 + num2 + num3

#def main():
#    n1 = float(input("Primeiro número = "))
#    n2 = float(input("Segundo número = "))
#    n3 = float(input("Terceiro número = "))
#    print (soma(n1, n2, n3))

#main()

# For / Listas ----------------------------------------

#animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
#animais[1+1] = "piriquito"
#animais[-3] = "piriquito"
#print(animais)

#for x in range(len(animais)):
#    print("--> ", x)

#for x in animais:
#    print("--> ", x)

#for x in range(len(animais)):
#    print("--> ", animais[x])

#for x in animais:
#    print("--> " + x)

#pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
#for x in range(5, 10):
#    print(pares[x])

#pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
#for x in range(len(pares)):
#    print(pares[x])

#lista=["cachorro","gato","papagaio","lebre","zebra"]
#print(lista.index("lebre"))
#for i in lista:
#	print(list(i))


# Classe ----------------------------------------
#class Pato:
#  pass

#pato = Pato()
#patinho = Pato()
#if pato == patinho:
#  print("Estamos no mesmo endereço!")
#else:
#  print("Estamos em endereços diferentes!")

#Files ----------------------------------------

#create a note from another note
f1 = open(r'C:\Users\drr19\Desktop\companies.txt')

cNames = f1.readlines()
for i in range(0,len(cNames)):
	cNames[i] = str(i+1)+' '+cNames[i]
f1.close()

#newcName = raw_input('Enter the name of new company: ')

f2 =open(r'C:\Users\drr19\Desktop\scompanies.txt','w')
f2.writelines(cNames)
f2.close()

#insert a title(or any other line) to a note that is already saved
f2 =open(r'C:\Users\drr19\Desktop\scompanies.txt','r+')
content =f2.read()
f2.seek(0,0)
f2.write("Output".rstrip('\r\n') + '\n' + content)
f2.close()


# Internet ----------------------------------------

#import urllib

#r = urllib.request.urlopen('https://www.google.com.br/')
#html = r.read()

#The “os” module in Python provides functions for file execution and directory handling operations, like file renaming and deletion.
#import os
#os.rename(current_file_name, new_file_name) #rename a file
#os.remove(file_name) # delete a file
#os.mkdir(newdir) # create a directory
#os.chdir(newdir) # change a directory
#os.getcwd() # acquire the current route
#os.rmdir(dirname) #delete a directory