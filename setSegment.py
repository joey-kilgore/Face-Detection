import RPi.GPIO as gpio
from time import sleep

numToPins = {0:[2,3,4,5,6,7],1:[3,4],2:[2,3,5,6,8],3:[2,3,4,5,8],4:[3,4,7,8],5:[2,4,5,7,8],6:[2,4,5,6,7,8],7:[2,3,4],8:[2,3,4,5,6,7,8],9:[2,3,4,7,8]}

def setup():
	gpio.setmode(gpio.BCM)
	for pinNum in range(2,9):
		gpio.setup(pinNum, gpio.OUT)
	gpio.setup(9,gpio.IN)

def setDisplay(num):
	global numToPins
	for pinNum in range(2,9):
		gpio.output(pinNum,0)

	for pinNum in numToPins[num]:
		gpio.output(pinNum,1)

setup()
while True:
	for num in range(0,10):
		setDisplay(num)
		inputVal = gpio.input(9)
		while inputVal == 1:
			inputVal = gpio.input(9)
			sleep(.005)
		#sleep(.05)

setDisplay(0)
