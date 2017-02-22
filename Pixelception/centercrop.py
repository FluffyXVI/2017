from PIL import Image

def CropCenter( image ):
	img = Image.open( image )
	w, h = img.size
	crop = 0
	if w > h:
		xx = (w-h)/2
		crop = img.crop( (xx, 0, xx+h, h) )
	else:
		yy = (h-w)/2
		crop = img.crop( (0, yy, w, yy+w) )
	
	crop.save( "cropped.png", "PNG" )
	
if __name__ == "__main__":
	filename = input("Filename: ")
	AverageImageFolder( filename )