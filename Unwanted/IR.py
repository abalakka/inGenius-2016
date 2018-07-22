import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.IN)
while True:
	i=GPIO.input(13)
	print i
	time.sleep(2)
