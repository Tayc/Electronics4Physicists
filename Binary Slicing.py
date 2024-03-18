#written by TAC F2022
#Splitting an 8-bit binary string into an array of invidual 1's & 0's
# these the values can be assigned to the indivual pins to put them high or low.
import numpy as np
binStr = '00101010'

#enable to check string initalized correctly
print(binStr[4])

pinStatus = np.empty((8), dtype=int)
#enable to check array initalizing properly
#print(pinStatus)

#this loop takes the binary string and uses a for loop to cycle all the binary values to
#assign to a record in the array
for i in range(0,8):
    pinStatus[i] = binStr[i]
    print(pinStatus[i])
    
print(pinStatus)