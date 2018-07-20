import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.IN)
#2 is the PIN number of GPIO port on Raspberry PI

streaming = False

def startStream():
    print("Stream Started")

def stopStream():
    print("Stream Stopped")

while True:
    #If input is equal to 1 then the beam is not broken
    #if input is equal to 0 then the beam is broken
    if(GPIO.input(2) ==1):
        print("Drive")
        time.sleep(1)

        if streaming:
            stopStream()
            streaming = False

    if(GPIO.input(2) ==0):
        print("Reverse")
        time.sleep(1)

        if not streaming:
            startStream()
            streaming = True
