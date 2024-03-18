#Written by TAC F2022
# this program reads the GPIO pins on the raspiberry pi and saves the values to an array
# we use the gpio library because it allows us low level controll of the pins
# to make sure the program runs at the correct speed, makes sure you do not
# have other programs running on the pi

#import al the packages we need, they should be preinstalled.
import RPi.GPIO as GPIO
import time
from time import sleep


file = open("mybinarysound2.txt","a") # creates the file that will store the ADC data

pinVal = [] # creates an array to hold the pin values

pins = [1,2,3,4,5,6,7,8] # the RPi pins that are connected to the ADC

GPIO.setmode(GPIO.BCM) # sets the pin reference system 

#checks pin numbering system is correct
#print(GPIO.getmode())
pPin = 0 # priming pin will be used to prime the ADC
GPIO.setup(pPin,GPIO.OUT) #sets up the prming pin
GPIO.setup(pins,GPIO.IN) #sets up all the read pins
GPIO.output(pPin, GPIO.HIGH) #primes the ADC
#we will use a time object to controll how long the loop runs
t_end = time.time() + 5 # current time * seconds * minutes
while time.time() < t_end: #this loop is clocked to run at ~10.2khz
    GPIO.output(pPin, GPIO.LOW)  #triggers the ADC, this ADC triggers on the falling edge 
    sleep(.00001) #waits 10 microseconds for the ADC to process and output data
    for i in range(1,9): #reads all the pins, appends their values to a list
        pinVal.append(GPIO.input(i))
    GPIO.output(pPin, GPIO.HIGH) #primes the ADC
GPIO.output(pPin, GPIO.LOW) #sets the ADC to standby
#print(pinVal)
NBytes = int(( len(pinVal) / 8 ))
#print(NBytes)
record = ''
print(time.time())
print('\n')
#the following loop processes the data using the pop method
for l in range(0,NBytes): #this loop takes a very long time. it took about 15 minutes to process 10 seconds of data
    for i in range(0,8):
        record += str(pinVal.pop(0))
    file.write("\n " + str(int(record,2))) #writes the record to a new line in the file 
#    print("\n " + record + " " + str(int(record,2)))
    record = ''
print("done at ")
print(time.time())
print('\n')
print(pinVal)
file.close()