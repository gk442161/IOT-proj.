import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
trig=23
echo=24
print("Distance Measurement in progress")

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)


GPIO.OUTPUT(trig,False)
print("Wating for sensor to settle")
time.sleep(2)


GPIO.OUTPUT(trig,True)
time.sleep(0.00001)
GPIO.OUTPUT(trig,False)

while GPIO.input(echo)==0:
    pulse_start=time.time()
while GPIO.input(echo)==1:
    pulse_end=time.time()

pulse_duration=pulse_end-pulse_start
distance=pulse_duration*17150

distance=round(distance,2)
print("Distance: ",distance,"cm")

GPIO.cleanup()