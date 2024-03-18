# Written TAC F2022
#In python, binary values are represented by the prefix '0b'
# python will automatically turn binary strings into integer values via print()
# this however does not help if we wish to use the binary values without the print function,


print(0b00101010)
# so we will use the int() funtion. we have to tell the int function what the numeric base is
# the base for binary is 2
binary = int('00101010',2)
print(binary)
#print(int(binStr,2))checks to see if you can go from binary string straight to int
