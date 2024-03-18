#Written by TAC F2022
#this program reads a binary list and then outputs thses values to the GPIO
#to light up LEDs

import RPi.GPIO as GPIO

pins = [1,2,3,4,5,6,7,8] # defines the RPi pins that are connected to the ADC, if you are not using these pins just change the numbers
pinVal = [1,0,1,0,1,0,1,0] # creates an array to hold the pin values, set these 8 bits to the binary representation of an int
print(0b10101010) #make sure this binary representation matches the one above (after the 0b), otherwise it will not print the correct integer
GPIO.setmode(GPIO.BCM) # sets the pin reference system 

#uncomment following line to make sure the pin numbering system is correct
#print(GPIO.getmode())

GPIO.setup(pins,GPIO.OUT) #sets up all the read pins
for g in range(0,8): #if the value of of the entry is 1 make the pin high, else make it low 
    if pinVal[g] == True: 
        GPIO.output(pins[g], GPIO.HIGH)
        print('HIGH ')
    else:  
        GPIO.output(pins[g], GPIO.LOW)
        print('LOW ')
print("Make sure the LEDs coresspond to the binary representation of your chosen integer!")
