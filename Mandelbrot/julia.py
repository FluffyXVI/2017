from PIL import Image

resolution = 256
quality = 25

px = 4 / (resolution-1)

# Adjust colors
rmod = 0.5
gmod = 1
bmod = 2

creal = float(input("Real: "))
cimagine = float(input("Imaginary: "))

img = Image.new( 'RGB', ( resolution, resolution ), "black")
pixels = img.load()

for i in range( img.size[0] ):
	ureal = (px * i) - 2
	for j in range( img.size[1] ):
		treal = ureal
		timagine = (px *j) - 2
		iterations = 0
		while abs( timagine ) < 2 and abs( treal ) < 2 and iterations < quality:
			nreal = ( ( treal*treal ) - ( timagine * timagine ) ) + creal
			timagine = (2 * treal * timagine) + cimagine
			treal = nreal
			iterations = iterations + 1
		
		qc = int( iterations * ( 256/quality) )
		col = ( int( qc * rmod ), int( qc * gmod ), int(qc * bmod ) )
		if iterations == quality:
			col = ( 0, 0, 0 )
		pixels[ i, j ] = col

img.save( "julia/" + str(creal) + ", " + str(cimagine) + "i.png", "PNG" )