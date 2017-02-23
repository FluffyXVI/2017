# Robert Fraser 2017
from PIL import Image

# With these two functions, any powers can be calculated
def SquareValue( r, i ):
	# a+bi squared = ( a squared - b squared ) + ( 2abi )
	n = (( r*r ) - ( i*i ))
	i = 2*r*i
	return n, i
	
def CubeValue( r, i ):
	# a+bi cubed = a cubed + 3a squared bi - 3a b squared - b cubed i
	# Maths is great
	n = (r**3) - (3*r*i*i)
	i = (3*r*r*i) - (i*i*i)
	return n, i
	
def ComplexPower( r, i, power ):
	# Mixes the above two functions to work with any power.
	while power > 1:
		if power % 3 == 0:
			r, i = CubeValue( r, i )
			power -= 3
		elif power % 2 == 0:
			r, i = SquareValue( r, i )
			power -= 2
		else:
			break
	return r, i
	
def AddComplex(*args):
	n = 0
	i = 0
	for each in args:
		n += each[0]
		i += each[1]
	return n, i
	
def SubtractComplex(*args):
	n = 0
	i = 0
	for each in args:
		n -= each[0]
		i -= each[1]
	return n, i
	
def InverseComplex( r, i ):
	return ( -r, -i )

# This function can be changed to create very different Mandelbrot sets	
def IteratePixel( real, imagine ):
	tr = 0
	ti = 0
	iterations = 0
	# tr represents the real component
	# ti represents the imaginary componenent
	# Iterate the value until the quality has been reached or it has 'escaped'
	while abs( ti ) < 2 and abs( tr ) < 2 and iterations < quality:
		tr, ti = SquareValue( tr, ti )
		tr, ti = AddComplex( (tr,ti), (real,imagine) )
		iterations = iterations + 1
	return iterations

# Iterate each pixel and color accordingly
def GenerateMandelbrot(**kwargs):
	print( kwargs )
	resolution = kwargs.get('resolution', 256)
	quality = kwargs.get('quality', 32)
	img = kwargs.get('image', Image.new( 'RGB', ( resolution, resolution ), "black"))
	pixels = img.load()
	func = kwargs.get('function', IteratePixel)
	colors = kwargs.get('color', (0.5, 1, 2))
	center = kwargs.get('center', (-0.7, 0))
	radius = kwargs.get('radius', 1.25)
	
	# Calculations for number to pixel
	startx = center[0] - radius
	starty = center[1] - radius

	ic = radius / ( (resolution-1) * 0.5 )
	
	for xx in range( img.size[0] ):
		creal = startx + (ic*xx)
		for yy in range( img.size[1] ):
			cimagine = starty + (ic*yy)
			iterations = func( creal, cimagine )
			
			qc = int( iterations * ( 256/quality) )
			col = ( int( qc * colors[0] ), int( qc * colors[1] ), int(qc * colors[2] ) )
			if iterations == quality:
				col = ( 0, 0, 0 )
			pixels[ xx, yy ] = col
	return img
		
if __name__ == "__main__":
	# Configurable settings if run directly
	center = (float(input("CenterX: ")), float(input("CenterY: ")))
	radius = float(input("Radius: "))
	color = (0.5, 1, 2)
	resolution = int(input("Resolution: "))
	quality = int(input("Quality: "))
	output = GenerateMandelbrot(center=center, radius=radius, color=color, resolution=resolution, quality=quality)
	output.save( "mandelbrot.png", "PNG" )