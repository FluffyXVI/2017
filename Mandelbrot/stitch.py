from PIL import Image
import os
import math

files = os.listdir( 'julia' )
for file in files:
	if not( file.endswith( ".png" ) ):
		print( file )
		files.remove( file )

grid = int( math.sqrt( len( files ) ) )
grid = 9
resolution = 256

canvas = Image.new( 'RGB', ( resolution*grid , resolution*grid ), "black")

for file in files:
	c = file.split( ", " )
	x = float( c[0] ) + 2
	y = float( c[1][:-5] ) + 2
	cx = int( x * resolution * 2 )
	cy = int( y * resolution * 2 )
	canvas.paste( Image.open( 'julia/' + file ), (cx, cy) )
	
canvas.save( "stitch_min.png", "PNG" )