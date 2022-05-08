import numpy as np

def gradiente(f,x,h=10**-6):
	if not isinstance(x, tuple):
		print("not a tuple! (grad)")

	g = np.empty(2)
	g[0] = (f([x[0]+h,x[1]])-f([x[0]-h,x[1]]))/(2*h)
	g[1] = (f([x[0],x[1]+h])-f([x[0],x[1]-h]))/(2*h)

	return g

def hessiano(f,x,h=10**-6):
	if not isinstance(x, tuple):
		print("not a tuple! (hess)")

	H = np.empty(4)
	shape = (2,2)
	H[0,0] = (f([x[0]+2*h,x[1]])+f([x[0]-2*h,x[1]])-2*f([x[0],x[1]]))/(4*h**2)
	H[1,1] = (f([x[0],x[1]+2*h])+f([x[0],x[1]-2*h])-2*f([x[0],x[1]]))/(4*h**2)
	H[0,1] = (f([x[0]+h,x[1]+h])-f([x[0]-h,x[1]+h])-f([x[0]+h,x[1]-h])+f([x[0]-h,x[1]-h]))/(4*h**2)
	H[1,0] = H[0,1]

	return H

def norma(w):
	return w[0]**2+w[1]**2

def newton(f,x0,epsilon=10**-6):
	if not isinstance(x0, tuple):
		print("not a tuple!")

	diff = 1
	grad = [1,1]
	y0 = np.array([x0[0], x0[1]])
	i=0

	while ( (diff > epsilon) or (norma(grad) > epsilon) ):
		i=i+1
		print("===========================")
		print(i)

		grad = gradiente(f,y0)
		H = hessiano(f,y0)

		y = np.empty(2)
		np.copyto(y, y0 - np.dot(np.linalg.inv(H),grad))

		print(y)

		print(y0)

		print(norma(grad))

		diff = norma((y[0]-y0[0], y[1]-y0[1]))
		print(diff)

		y0 = np.empty(2)
		np.copyto(y0,y)

	return (y[0],y[1])

def f(x):
	return -(x[0]-5)**4-(x[1]-6)**4

x0 = (0,0)
newton(f,x0)
