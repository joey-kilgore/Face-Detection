import RPi.GPIO as gpio

numToPins = {0:[2,3,4,5,6,7],1:[3,4],2:[2,3,5,6,8]}

def setup():
	gpio.setmode(gpio.BCM)
	for pinNum in range(2,9):
		gpio.setup(pinNum, gpio.OUT)

def setDisplay(num):
	global numToPins
	for pinNum in range(2,9):
		gpio.output(pinNum,0)

	for pinNum in numToPins[num]:
		gpio.output(pinNum,1)

setup()
setDisplay(0)
