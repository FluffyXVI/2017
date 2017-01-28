from PIL import Image
import os

def AverageImageFolder( dir ):
	for file in os.listdir( dir ):
		# Open the image and resize it to 512x512
		img = Image.open( dir + "/" + file )
		img.thumbnail( (512, 512) )
		result = img
		px = img.load()
		w, h = img.size
		rr, gg, bb, count = 0, 0, 0, 0
		# Add the total values for every pixel
		for xx in range( w ):
			for yy in range( h ):
				color = px[xx, yy]
				rr += color[0]
				gg += color[1]
				bb += color[2]
				count += 1
		# Average the values out
		color = ( rr//count, gg//count, bb//count )
				
		# Save the image into the palette folder with the color name
		name = str(color[0]) + "," + str(color[1]) + "," + str(color[2])
		result.save( "palette/" + name + ".png", "PNG" )
		# Save the color into the pure folder
		img.paste( color, (0,0,w,h) )
		img.save( "pure/" + name + ".png", "PNG" )
		
if __name__ == "__main__":
	folder = input("Input folder: ")
	AverageImageFolder( folder )