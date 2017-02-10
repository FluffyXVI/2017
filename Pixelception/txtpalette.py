from PIL import Image

hexc = { '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F': 15 }
def HexConversion( hex ):
	hex = hex.upper()
	if hex[0] == "#":
		hex = hex[1:]
	red = hexc[hex[0]]*16 + hexc[hex[1]]
	green = hexc[hex[2]]*16 + hexc[hex[3]]
	blue = hexc[hex[4]]*16 + hexc[hex[5]]
	return ( red, green, blue )
	
def RGBTuple( rgb ):
	if rgb[0:4] == "rgb(":
		rgb = rgb[5:-1]
	rgb = rgb.split(",")
	return ( int(rgb[0]), int(rgb[1]), int(rgb[2]) )
	
def PaletteFromText( file ):
	palette = []
	for line in open( file ):
		line = line.strip()
		color = (255, 255, 255)
		if line[0] == "!":
			continue
		# Hexadecimal color
		if line[0] == "#":
			color = HexConversion( line )
		elif line[0:4] == "rgb(":
			color = RGBTuple( line )
		elif len(line) == 6:
			color = HexConversion( line )
		else:
			color = RGBTuple( line )
		palette.append( color )
	return palette