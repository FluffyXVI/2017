import mandelbrot

def IteratePixel( real, imagine, quality, *extra ):
	tr = 0
	ti = 0
	iterations = 0
	# tr represents the real component
	# ti represents the imaginary componenent
	# Iterate the value until the quality has been reached or it has 'escaped'
	while abs( ti ) < 2 and abs( tr ) < 2 and iterations < quality:
		tr, ti = mandelbrot.ComplexPower( tr, ti, extra[0] )
		tr, ti = mandelbrot.AddComplex( (tr,ti), (real,imagine) )
		iterations = iterations + 1
	return iterations

for i in range(2, 10):
	img = mandelbrot.GenerateMandelbrot( function=IteratePixel, extra1=i, resolution=512 )
	img.save('mandelbrot' + str(i) + '.png', 'PNG' )