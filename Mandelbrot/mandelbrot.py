# Robert Fraser 2017
from PIL import Image

def SquareValue( r, i ):
	return ComplexPower( r, i, 2 )
	
def ComplexPower( r, i, power ):
	# Multiplication is great
	nr = r
	ni = i
	power -= 1
	while power >= 1:
		nr, ni = MultiplyComplex( (nr, ni), (r, i) )
		power -= 1
	return nr, ni
	
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
	
def MultiplyComplex( c1, c2 ):
	# (ac - bd) + (ad + bc)i
	return (c1[0] * c2[0]) - (c1[1] * c2[1]), (c1[0] * c2[1]) + (c1[1] * c2[0])
	
def InverseComplex( r, i ):
	return -r, -i

# This function can be changed to create very different Mandelbrot sets	
def IteratePixel( real, imagine, quality, *extra ):
	tr = 0
	ti = 0
	iterations = 0
	# tr represents the real component
	# ti represents the imaginary componenent
	# Iterate the value until the quality has been reached or it has 'escaped'
	while abs( ti ) < 2 and abs( tr ) < 2 and iterations < quality:
		tr, ti = ComplexPower( tr, ti, 2 )
		tr, ti = AddComplex( (tr,ti), (real,imagine) )
		iterations = iterations + 1
	return iterations

# Iterate each pixel and color accordingly
def GenerateMandelbrot(**kwargs):
	resolution = kwargs.get('resolution', 256)
	quality = kwargs.get('quality', 32)
	img = kwargs.get('image', Image.new( 'RGB', ( resolution, resolution ), "black"))
	pixels = img.load()
	func = kwargs.get('function', IteratePixel)
	colors = kwargs.get('color', (0.5, 1, 2))
	center = kwargs.get('center', (0, 0))
	radius = kwargs.get('radius', 1.5)
	extra1 = kwargs.get('extra1', None)
	extra2 = kwargs.get('extra2', None)
	
	# Calculations for number to pixel
	startx = center[0] - radius
	starty = center[1] - radius

	ic = radius / ( (resolution-1) * 0.5 )
	
	for xx in range( img.size[0] ):
		creal = startx + (ic*xx)
		for yy in range( img.size[1] ):
			cimagine = starty + (ic*yy)
			iterations = func( creal, cimagine, quality, extra1, extra2 )
			
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