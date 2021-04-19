import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
servo=GPIO.PWM(17,50)
servo.start(0)
time.sleep(1)
duty =2

while duty<=12:
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    duty=duty+1
    
time.sleep(2)

while duty>=0:
    servo.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty=duty-1
    
servo.stop()
GPIO.cleanup()
print('done')
