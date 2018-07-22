
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)

p = GPIO.PWM (11, 50)

p.start (1.5)

p.ChangeDutyCycle(10.5)
#time.sleep(1)
#p.ChangeDutyCycle(1.5)
#time.sleep(1)


