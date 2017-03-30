from PIL import Image, ImageDraw
import random
import math

def CreatePolys( width, height, c, v ):
	points = {}
	
	for xx in range(0, width, c):
		if not xx//c in points:
			points[xx//c] = {}
			
		for yy in range(0, height, c):
			px = (xx + c/2) + (random.uniform(-1, 1) * v)
			py = (yy + c/2) + (random.uniform(-1, 1) * v)
			points[xx//c][yy//c] = (math.floor(px), math.floor(py))
	
	return points
	
def GetColor( max, x, y, v ):
	fracx = x/max + random.uniform(-v, v)
	fracy = y/max
	rchange = rmax - rmin
	gchange = gmax - gmin
	bchange = bmax - bmin
	return ( math.floor(rchange*fracx) + rmin, math.floor(gchange*fracx) + gmin, math.floor(bchange*fracx) + bmin )
		
	
def CreatePolyImage( size, cell, vrate, angle ):
	grid = CreatePolys( size+cell+cell, size+cell+cell, cell, cell/2.25 )
	img = Image.new( 'RGB', ( size+cell+cell, size+cell+cell ), 'black' )
	px = img.load()
	d = ImageDraw.Draw(img)

	for row in grid:
		for point in grid[row]:
			if row+1 in grid and point+1 in grid[row]:
				p1 = grid[row][point]
				p2 = grid[row+1][point]
				p3 = grid[row][point+1]
				d.polygon( [ (p1[0], p1[1]), (p2[0], p2[1]), (p3[0], p3[1]) ], GetColor( size/cell, row, point, 0.05 ) )
				
				p1 = grid[row][point+1]
				p2 = grid[row+1][point]
				p3 = grid[row+1][point+1]
				d.polygon( [ (p1[0], p1[1]), (p2[0], p2[1]), (p3[0], p3[1]) ], GetColor( size/cell, row+0.15, point+0.15, 0.1 ) )
	img = img.rotate( angle )
	img = img.crop( (cell, cell, cell+size, cell+size) )
	return img

if __name__ == "__main__":
	for i in range(100):
		rmin = random.randint( 0, 12 ) * 10
		rmax = rmin + random.randint( 0, 12 ) * 10
		gmin = random.randint( 0, 12 ) * 10
		gmax = gmin + random.randint( 0, 12 ) * 10
		bmin = random.randint( 0, 12 ) * 10
		bmax = bmin + random.randint( 0, 12 ) * 10
		
		angle = random.choice( [0, 90, 180, 270] )
		CreatePolyImage( 512, 46, 2.25, angle ).save( 'gen/' + str(i) + '.png' )