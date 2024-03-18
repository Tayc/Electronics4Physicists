#pop method test
popper = [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1]
#popper.pop(0)
file = open("mypopper.txt","a")
record = ''
for l in range(0,2):
    for i in range(0,8):
        record += str(popper.pop(0))
    file.write("\n " + str(int(record,2))) #writes the record to a new line in the file 
    print("\n " + record + " " + str(int(record,2)))
    record = ''
print(popper)
file.close()