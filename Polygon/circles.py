from PIL import Image, ImageDraw
import random
import math

def GenerateCircle( px, a, b, radius, color ):
	ras = radius**2
	for xx in range( a-radius, a+radius ):
		for yy in range( b-radius, b+radius ):
			val = (xx-a)**2 + (yy-b)**2
			if val < ras:
				px[xx, yy] = color


size = 512
img = Image.new( 'RGB', ( size, size ), 'white' )
px = img.load()

r1 = random.randint( 0, 255 )
r2 = random.randint( 0, 255 )
rmax = max(r1, r2)
rmin = min(r1, r2)

g1 = random.randint( 0, 255 )
g2 = random.randint( 0, 255 )
gmax = max(g1, g2)
gmin = min(g1, g2)

b1 = random.randint( 0, 255 )
b2 = random.randint( 0, 255 )
bmax = max(b1, b2)
bmin = min(b1, b2)

rchange = rmax - rmin
gchange = gmax - gmin
bchange = bmax - bmin

radius = 24
gap = 4
count = size//(radius+radius+gap)
circles = (radius*2*count) + gap*(count-1)
edge = (size-circles)//2
for xx in range(radius+edge, 512, radius*2 + gap):
	fracx = xx/size
	for yy in range(radius+edge, 512, radius*2 + gap):
		GenerateCircle( px, xx, yy, radius, ( math.floor(rchange*fracx) + rmin, math.floor(gchange*fracx) + gmin, math.floor(bchange*fracx) + bmin ) )
		
		
img.save('test.png')