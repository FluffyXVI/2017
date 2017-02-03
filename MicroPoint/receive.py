import serial
import pyautogui as gui
c = serial.Serial('COM4', 9600)

lm = False
rm = False

while True:
	# Input should be read in the form x,y,a,b
	# X and Y are integer values
	# A and B are either "True" or "False"
	line = c.readline().decode('UTF-8')[:-1]
	line = line.split(",")
	xx = int( line[0] )
	yy = int( line[1] )
	aa = line[2]
	if aa == "True":
		aa = True
	else:
		aa = False
		
	bb = line[3]
	if bb == "True":
		bb = True
	else:
		bb = False
		
	if abs(xx) < 100:
		xx = 0
	if abs(yy) < 100:
		yy = 0
	gui.moveRel( xx//16, yy//16, 0.1 )
	try:
		if aa and not lm:
			lm = True
			gui.mouseDown(button='left')
		elif lm and not aa:
			lm = False
			gui.mouseUp(button='left')
		if bb and not rm:
			rm = True
			gui.mouseDown(button='right')
		elif rm and not bb:
			rm = False
			gui.mouseUp(button='right')
	except:
		pass