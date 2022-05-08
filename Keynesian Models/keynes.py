class modeloslineares():

	def keynes1(a0=20,a1=0.7,b0=80,b1=-250,g0=15,g1=0.2,k=0.15,d0=10,d1=-20,G=95,MP=70,X=15,IM=5):
		#Manuel Alcino da Fonseca (Manole, 2003, apêndice 2B)
		#variáveis exógenas: estas equações são dadas ou imediatamente estimadas -> valores padrão do livro
		#o autor também apresenta um modelo baseado em kalecki (muito similar ao modelo de Keynes, mas criando dois grupos de consumidores, cada qual com suas propensões marginais, com base em salário e lucro)
		#os modelos de Keynes e kalecki são estáticos; Klein (1950) desenolve uma versão dinâmica no mesmo espírito -> temos equações simultâneas resolvidas por MQ2E
		#M/P é representado como uma única variável MP para que o sistema seja linear
		#Modelo Keynesiano estimado:
		#Y = C + I + G + X - IM
		#C = a0 + a1*(Y-T)
		#I = b0 + b1*r
		#T = g0 + g1*Y
		#MP = k*Y + d0 + d1*r
		#Equação: B*y + Gamma*x = 0 --->>> y = (-1)*(B^(-1))*Gamma*x

		from numpy.linalg import inv
		from operacoesmatrizes import multmatrizes
		from operacoesmatrizes import multescalar

		Gamma = [[0,1,0,1],[a0,0,0,0],[b0,0,0,0],[g0,0,0,0],[d0,0,-1,0]]
		B = [[-1,1,1,0,0],[a1,-1,0,-a1,0],[0,0,-1,0,b1],[g1,0,0,-1,0],[k,0,0,0,d1]]
		x = [[1],[G],[MP],[X-IM]]
		y = [Y,C,I,T,r] = multescalar(multmatrizes(multmatrizes(inv(B),Gamma),x),-1)

		#definições de IS-LM (r de equilíbrio já é calculado em y)
		#r_IS = (a0-a1*g0+b0+G+X-IM)/(-1*b1) - (1-a1*(1-g1))*Y[0]/(-b1)
		#r_LM = (d0-MP)/(-1*d1) + k/(-1*d1)*Y[0]
		
		#retorno mais apresentável
		for i in range(len(y)): y[i] = y[i][0]

		return(y)

	def kalecki1(a0=20,a1=0.85,g1=0.25,a2=0.55,g2=0.35,b0=80,b1=0.3,b2=-250,d=0.2,d0=10,d1=0.15,d2=-20,G=95,X=55,IM=45,MP=70):
		#Manuel Alcino da Fonseca (Manole, 2003, apêndice 2B)
		#Modelo Kaleckiano estimado:
		#Y = C + I + G + X - IM
		#C = a0 + a1*(1-g1)*W + a2*(1-g2)*Pi
		#I = b0 + b1*P + b2*r
		#Pi = d*(W+IM)
		#W = Y - Pi - T
		#T = g1*W + g2*Pi
		#MP = d0 + d1*Y + d2*r
		#Equação: B*y+Gamma*x=0 --->>> y = (-1)*(B^(-1))*Gamma*x

		from numpy.linalg import inv
		from operacoesmatrizes import multmatrizes
		from operacoesmatrizes import multescalar

		#a1 e a2 na equação de B precisam ser corrigidos

		Gamma = [[0,1,1,-1,0],[a0,0,0,0,0],[b0,0,0,0,0],[0,0,0,d,0],[0,0,0,0,0],[0,0,0,0,0],[d0,0,0,0,-1]]
		B = [[-1,1,1,0,0,0,0],[0,-1,0,a2,a1,0,0],[0,0,-1,b1,0,0,b2],[0,0,0,-1,d,0,0],[1,0,0,-1,-1,-1,0],[0,0,0,g2,g1,-1,0],[d1,0,0,0,0,0,d2]]
		x = [[1],[G],[X],[IM],[MP]]
		y = [Y,C,I,Pi,W,T,r] = multescalar(multmatrizes(multmatrizes(inv(B),Gamma),x),-1)

		#retorno mais apresentável
		for i in range(len(y)): y[i] = y[i][0]

		return(y)

	#def klein1(a0=20,a1=0.85,g1=0.25,a2=0.55,g2=0.35,b0=80,b1=0.3,b2=-250,d=0.2,d0=10,d1=0.15,d2=-20,G=95,X=55,IM=45,MP=70):
		#Manuel Alcino da Fonseca (Manole, 2003, apêndice 2B)
		#Modelo Kaleckiano estimado:
		#Y = C + I + G + X - IM
		#C = a0 + a1*(1-g1)*W + a2*(1-g2)*Pi
		#I = b0 + b1*P + b2*r
		#Pi = d*(W+IM)
		#W = Y - Pi - T
		#T = g1*W + g2*Pi
		#MP = d0 + d1*Y + d2*r
		#Equação: B*y+Gamma*x=0 --->>> y = (-1)*(B^(-1))*Gamma*x
	#	from numpy.linalg import inv
	#	from operacoesmatrizes import multmatrizes
	#	from operacoesmatrizes import multescalar
	#	Gamma = [[a0,a2,0,0,0,a3,0,0],[b0,0,0,0,0,b2,b3,0],[g0,-g1,g1,0,g3,0,0,g2],[0,0,-1,1,0,0,0,0],[0,-1,0,0,0,0,0,0],[0,0,0,0,0,0,1,0]]
	#	B = [[-1,0,a2,0,a1,0],[0,-1,0,0,1,b1,0],[0,0,-1,g1,0,0],[1,1,0,-1,0,0],[0,0,-1,1,-1,0],[0,1,0,0,0,-1]]
	#	x = [[1],[W2],[T],[G],[t-1931],[Piant],[Kant],[(Y-T+W2)ant]]
	#	y = [Y,C,I,W1,Yd,Pi,K] = multescalar(multmatrizes(multmatrizes(inv(B),Gamma),x),-1)	
		#retorno mais apresentável
	#	for i in range(len(y)): y[i] = y[i][0]
	#	return(y)