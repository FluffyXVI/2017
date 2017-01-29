from PIL import Image

resolution = 256
quality = 25
step = float(input("Step Size: "))

px = 4 / (resolution-1)

rmod = 0.5
gmod = 1
bmod = 2

creal = -2
ccomplex = -2

while creal <= 2:
	while ccomplex <= 2:
		img = Image.new( 'RGB', ( resolution, resolution ), "black")
		pixels = img.load()
		
		for i in range( img.size[0] ):
			ureal = (px * i) - 2
			for j in range( img.size[1] ):
				treal = ureal
				tcomplex = (px *j) - 2
				iterations = 0
				while abs( tcomplex ) < 2 and abs( treal ) < 2 and iterations < quality:
					nreal = ( ( treal*treal ) - ( tcomplex * tcomplex ) ) + creal
					tcomplex = (2 * treal * tcomplex) + ccomplex
					treal = nreal
					iterations = iterations + 1
				
				qc = int( iterations * ( 256/quality) )
				col = ( int( qc * rmod ), int( qc * gmod ), int(qc * bmod ) )
				if iterations == quality:
					col = ( 0, 0, 0 )
				pixels[ i, j ] = col
		
		img.save( "julia/" + str(creal) + ", " + str(ccomplex) + "i.png", "PNG" )
		ccomplex = ccomplex + step
	ccomplex = -2
	creal = creal + step
	