from PIL import Image
import txtpalette

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
	
palette = txtpalette.PaletteFromText( input("Palette: ") )
base = Image.open( input('Image: ') )
w, h = base.size
px = base.load()

for xx in range(w):
	for yy in range(h):
		color = FindClosestColor( px[xx, yy] )
		px[xx, yy] = palette[color]

base.save( "colorclose.png", "PNG" )		