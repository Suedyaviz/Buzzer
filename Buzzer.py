import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
buzzer = 23

GPIO.setup(buzzer,GPIO.OUT)

while True:

   GPIO.output(buzzer, GPIO.HIGH)
print ("Beep")
sleep (0.1)

GPIO.output(buzzer, GPIO.LOW)
print("NO Beep")
sleep(0.3)
