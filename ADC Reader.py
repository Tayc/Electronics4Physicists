#Written by TAC F2022
#this program reads the GPIO pins on the raspiberry pi and saves the values to an array
#we use the gpio library because it allows us low level controll of the pins
import numpy as np
import RPi.GPIO as GPIO
import time
from time import sleep


file = open("mysound.csv","a") # creates the file that will store the ADC data

pinVal = np.empty((8),dtype=int) # creates an array to read the pin values

pins =[2,3,4,5,6,7,8,9] # the RPi pins that are connected to the ADC

GPIO.setmode(GPIO.BCM) # sets the pin reference system 

#checks pin numbering system is correct
#print(GPIO.getmode())
pPin = 12 # priming pin will be used to prime the ADC
GPIO.setup(pPin,GPIO.OUT) #sets up the prming pin
GPIO.setup(pins,GPIO.IN) #sets up all the read pins

GPIO.output(pPin, GPIO.LOW) #Primes the ADC to be read

# this is the loop that reads the ADC pins, converts to a number, then writes to file
p=0 #this is a dummy variab;e for testing. I reccomend using a while True loop, and crtl+c once you have recorded enough sound data 
while p < 400:
    GPIO.output(pPin, GPIO.HIGH)
    GPIO.output(pPin, GPIO.LOW) #these to lines prime the ADC to be read. the ADC triggers on the falling slope
    sleep(0.00001) #waiting 10 microseconds for the ADC to process
    pinVal = np.empty((8),dtype=int)
    for i in range(2,10): #reads all the pins
        pinVal[i-2]=GPIO.input(i)
    data = '' #resets the string to empty
    for l in range(0,8): #fills the string with binary
        data += str(pinVal[l])
    #the next 3 lines create the data record
    file.write(time.asctime( time.localtime(time.time()) )) #prints the time
    file.write(", " + str(int(data))) #writes the array
    file.write("\n") #writes new line
    p += 1

file.close()