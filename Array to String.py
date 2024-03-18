#written by TAC F2022
#Reading the pins (dummy array) to create the an array of binarys
# this array will then be turned into a string and then into an int
import numpy as np

#creates an empty string variable to store the binary values
binStr = ''

#just an dummy array for now. we'll get to pin reading soon enough!
pinStatus = np.empty((8), dtype=int)
#enable to check array initalizing properly
#print(pinStatus)

#this loop takes the pins and appends all the values together to create a string of binary
for i in range(0,8):
    binStr += str(pinStatus[i])
    print(binStr)

print(int(binStr)) # prints the string as an int