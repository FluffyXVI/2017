# Robert Fraser 2017
from PIL import Image

# Adjust view window
centerx = float(input("CenterX: "))
centery = float(input("CenterY: "))
radius = float(input("Radius: "))

# Adjust colors
rmod = 0.5
gmod = 1
bmod = 2

# Adjust output quality
resolution = int(input("Resolution: "))
quality = int(input("Quality: "))

# Calculations for number to pixel
startx = centerx - radius
starty = centery - radius

ic = radius / ( (resolution-1) * 0.5 )

img = Image.new( 'RGB', ( resolution, resolution ), "black")
pixels = img.load()

def SquareValue( r, i ):
	# a+bi squared = ( a squared - b squared ) + ( 2abi )
	n = (( r*r ) - ( i*i ))
	i = 2*r*i
	return n, i

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
		tr += real
		ti += imagine
		iterations = iterations + 1
	return iterations

# Iterate each pixel and color accordingly
for xx in range( img.size[0] ):
	creal = startx + (ic*xx)
	for yy in range( img.size[1] ):
		cimagine = starty + (ic*yy)
		iterations = IteratePixel( creal, cimagine )
		
		qc = int( iterations * ( 256/quality) )
		col = ( int( qc * rmod ), int( qc * gmod ), int(qc * bmod ) )
		if iterations == quality:
			col = ( 0, 0, 0 )
		pixels[ xx, yy ] = col
		
img.save( "mandelbrot.png", "PNG" )	