def computador_escolhe_jogada(n,m):
	if n <= m:
		jogada_comp = n

	else:
		jogada_comp = m
		Pass = (((n-jogada_comp)%(m+1)==0))
		while not Pass:
			jogada_comp = jogada_comp - 1
			Pass = (((n-jogada_comp)%(m+1)==0) and (jogada_comp > 0))
			if jogada_comp == 0:
				jogada_comp = m
				break
			else:
				pass

	return jogada_comp

def pass_user(n,m,jogada_user):
	forbidden = (((n-jogada_user)<0) or (jogada_user>m) or (jogada_user<=0))
	#(((n-jogada_user) % (m+1)) == 0) or 
	return forbidden

def usuario_escolhe_jogada(n,m):
	jogada_user = int(input("Usuário, digite a sua jogada: "))
	while pass_user(n,m,jogada_user):
		print("Oops! Jogada inválida! Tente de novo.")
		jogada_user = int(input("Usuário, digite a sua jogada: "))
	return jogada_user

def partida():
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))

	if (n % (m+1) == 0) and (n>m):
		print("Voce começa!")
		while n > 0:
			x = usuario_escolhe_jogada(n,m)
			n = n - x
			print("Voce tirou",x,"peças.")
			print(n,"peças restantes")
			
			x = computador_escolhe_jogada(n,m)
			n = n - x
			print("O computador tirou",x,"peças.")
			print(n,"peças restantes")
	else:
		print("Computador começa!")
		while n > 0:
			x = computador_escolhe_jogada(n,m)
			n = n - x
			print("O computador tirou",x,"peças.")
			print(n,"peças restantes")
			
			if n > 0:
				x = usuario_escolhe_jogada(n,m)
				n = n - x
				print("Voce tirou",x,"peças.")
				print(n,"peças restantes")
			else:
				pass

	print("Fim do jogo! O computador ganhou!")

def campeonato():
	counter = 1
	while counter <= 3:
		print("**** Rodada",counter,"****")
		partida()
		counter = counter + 1

	print("**** Final do campeonato! ****"'\n'
		"Placar: Você 0 X 3 Computador")

#game----------------------------------------------
def run():

	print("Bem-vindo ao jogo do NIM! Escolha:"'\n'
		"1 - para jogar uma partida isolada"'\n'
		"2 - para jogar um campeonato")

	modo = int (input())

	if modo == 1:
		print("Voce escolheu uma partida!")
		partida()

	else:
		print("Voce escolheu um campeonato!")
		campeonato()

run()