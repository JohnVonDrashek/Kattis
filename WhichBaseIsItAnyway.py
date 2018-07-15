import sys

p = int(input(""))

for j in range(0, p):
    line = input("")
    k, num = line.split(" ")

    octnum = 0

    start = 0
    if int(num) < 0:
        start = 1
    
    for i in range(start, len(num)):
        digit = int(num[i])
        if digit >= 8:
            octnum = 0
            break
        else:
            octnum += digit * pow(8, len(num) - i - 1)


    hexnum = 0
    for i in range(start, len(num)):
        digit = int(num[i])
        hexnum += digit * pow(16, len(num) - i - 1)


    print(k, end="")

    if(int(num)< 0 and octnum != 0):
        print(" -" + str(octnum) + " " + str(int(num)) + " -" + str(hexnum))
    elif int(num) < 0:
        print(" " + str(octnum) + " " + str(int(num)) + " -" + str(hexnum))
    else:
        print(" " + str(octnum) + " " + str(int(num)) + " " + str(hexnum))
    
            
                 
