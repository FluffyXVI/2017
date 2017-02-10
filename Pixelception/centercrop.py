from PIL import Image

img = Image.open( input('File: ') )
w, h = img.size
crop = 0
if w > h:
	xx = (w-h)/2
	crop = img.crop( (xx, 0, xx+h, h) )
else:
	yy = (h-w)/2
	crop = img.crop( (0, yy, w, yy+w) )

crop.save( "cropped.png", "PNG" )