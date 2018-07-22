import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup (3, GPIO.OUT)
count = 0

while True:

        
        
	i = GPIO.input(26)
	j = GPIO.input(13)

	if i == 0 and j == 1:
		count = count + 1
	elif i == 1 and j == 0:

               if count != 0:
                        count = count - 1
        
      
	print "Count = " , count
	
	if count > 0:
		GPIO.output(GPIO.HIGH)

	else:
		GPIO.output(GPIO.LOW)
		
	time.sleep(0.3)
