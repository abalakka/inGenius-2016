import RPi.GPIO as GPIO
import time
import subprocess
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
GPIO.setup(13,GPIO.IN)


p = GPIO.PWM (11, 50)
p.start (2.5)

file1 = open("outputON",'r')
file2 = open("barcodeON",'r')
s=[]
i=0
for line1 in file1:
	s.append (line1)
for line2 in file2:
	s.append(line2)

if s[0]==s[1]:
	
	subprocess.call(["sh", "setInitialPos.sh"])
	
	while True:
		i=GPIO.input(13)
		time.sleep(1)
		if(i==1):
			break
	
	subprocess.call(["sh", "setFinalPos.sh"])


	          

	
