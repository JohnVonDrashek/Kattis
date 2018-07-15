import sys

line = input("")
numblack = 0
numwhite = 0


for i in line:
    if i == 'W':
        numwhite += 1
    if i == 'B':
        numblack += 1

if numblack == numwhite:
    print("1")
else:
    print("0")
