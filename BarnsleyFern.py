# Daniel Rocha Ruiz, MSc in Data Science and Business Analytics
# Source: Hill, C. (2016). Learning Scientific Programming with Python. Cambridge: Cambridge University Press. doi:10.1017/CBO9781139871754

def barnsleyfern(width=300,height=300,npts=50000):

	# Barnsley’s fern (Fractal)
	if npts > width*height: npts = width*height

	# import packages
	import numpy as np
	import matplotlib.pyplot as plt
	import matplotlib.cm as cm

	# define functions
	f1 = lambda x,y: (0., 0.16*y)
	f2 = lambda x,y: (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)
	f3 = lambda x,y: (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
	f4 = lambda x,y: (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)
	fs = [f1, f2, f3, f4]

	# set canvas size (pixels)
	aimg = np.zeros((width, height))

	# loop
	x, y = 0, 0
	for i in range(npts):
		# Pick a random transformation and apply it
		f = np.random.choice(fs, p=[0.01, 0.85, 0.07, 0.07])
		x, y = f(x,y)
		# Map (x,y) to pixel coordinates.
		# NB we "know" that -2.2 < x < 2.7 and 0 <= y < 10
		ix = int(width / 2 + x * width / 10)
		iy = int(y * height / 12)
		# Set this point of the array to 1 to mark a point in the fern
		aimg[iy, ix] = 1

	plt.imshow(aimg[::-1,:], cmap=cm.Greens)
	plt.show()

barnsleyfern()