import RPi.GPIO as GPIO
import time
import picamera
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG=18
ECHO=24
led=2

print("Distance measurement in progress....")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

while True:
	GPIO.output(TRIG,False)
	time.sleep(1)
	GPIO.output(TRIG,True)
	time.sleep(0.01)
	GPIO.output(TRIG,False)
	
	while GPIO.input(ECHO)==0:
		pulse_begin=time.time()
	
	while GPIO.input(ECHO)==1:
		pulse_end=time.time()
		
	pulse_duration=pulse_end-pulse_begin
	
	distance=pulse_duration*11150
	distance=round(distance,2)
	
	if distance>20:
		GPIO.output(led,GPIO.LOW)
		print('out of danger zone')
	else:
		GPIO.output(led,GPIO.HIGH)
		print('in danger zone')		
		camera = picamera.PiCamera()
		camera.start_preview()
		camera.start_recording('recorded.h264')
		camera.wait_recording(7)
		camera.stop_recording()
		camera.stop_preview()
		GPIO.output(led,GPIO.LOW)
		break
