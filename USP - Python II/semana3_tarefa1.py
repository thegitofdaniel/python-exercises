import pytest

class Triangulo:

	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c

	def perimetro(self):
		return(self.a+self.b+self.c)

	def tipo_lado(self):
		if self.a == self.b == self.c:
			return("equilátero")
		
		elif self.a == self.b or self.a == self.c or self.b == self.c:
			return("isóceles")

		else:
			return("escaleno")

	def retangulo(self):
		ordenado = sorted([self.a,self.b,self.c])
		retangulo = ((ordenado[0]**2 + ordenado[1]**2) == (ordenado[2]**2))
		return retangulo

	def semelhantes(self,t2):
		ordenado1 = sorted([self.a,self.b,self.c])
		ordenado2 = sorted([t2.a,t2.b,t2.c])
		if ordenado1[0]/ordenado2[0] == ordenado1[1]/ordenado2[1] == ordenado1[2]/ordenado2[2]:
			return True
		else:
			return False

@pytest.mark.parametrize("ent_a,ent_b,ent_c,tipo_lado", [
	(8,8,8,"equilátero"),
	(8,8,3,"isósceles"),
	(8,3,8,"isósceles"),
	(3,8,8,"isósceles"),
	(5,6,7,"escaleno"),
	(8,9,10,"escaleno")])

def testa_tipo_lado(ent_a,ent_b,ent_c,tipo_lado):
	assert tipo_lado(ent_a,ent_b,ent_c) == tipo_lado