from PIL import Image
import os

# Given a color, finds the closest match in the palette
def FindClosestColor( color ):
	best = 512
	cindex = -1
	for key,testcase in enumerate(palette):
		red = (color[0] - testcase[0])**2
		green = (color[1] - testcase[1])**2
		blue = (color[2] - testcase[2])**2
		difference = (red+green+blue)**0.5
		if difference < best:
			best = difference
			cindex = key
	return cindex

# Define quality of the image and the size of each pixel
quality = int(input("Quality: "))
imgsize = int(input("Pixel Size: "))

# Load the palette files into memory	
palette = []
palettefiles = []
for file in os.listdir( 'palette' ):
	img = Image.open( 'palette/' + file )
	img.thumbnail((imgsize,imgsize))
	palettefiles.append( img )
	file = file[:-4].split(",")
	palette.append( ( int(file[0]), int(file[1]), int(file[2]) ) )

base = Image.open( input('File: ') )
w, h = base.size
base.thumbnail( (w//quality, h//quality) )
base.save( "thumbnail.png", "PNG")
w,h = base.size
px = base.load()

canvas = Image.new( 'RGB', ( w*imgsize, h*imgsize ), "black" )

# For every pixel, find the matching image
for xx in range(w):
	for yy in range(h):
		color = FindClosestColor( px[xx, yy] )
		px[xx, yy] = palette[color]
		canvas.paste( palettefiles[color], (xx*imgsize,yy*imgsize) )
		
base.save( "converted.png", "PNG" )
canvas.save( "result.png", "PNG" )