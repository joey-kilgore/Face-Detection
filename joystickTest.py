import RPi.GPIO as gpio
from time import sleep

numToPins = {0:[2,3,4,5,6,7],1:[3,4],2:[2,3,5,6,8]}

def setup():
	gpio.setmode(gpio.BCM)
	for pinNum in range(2,5):
		gpio.setup(pinNum, gpio.IN)

def setDisplay(num):
	global numToPins
	for pinNum in range(2,9):
		gpio.output(pinNum,0)

	for pinNum in numToPins[num]:
		gpio.output(pinNum,1)

setup()
#setDisplay(0)
# pin 2 is y
# pin 3 is x
# pin 4 is b

while True:
	print("x,y " +str(gpio.input(3))+','+str(gpio.input(2)))
	print("b "+str(gpio.input(4)))
	sleep(.25)
