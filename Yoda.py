import sys

line1 = input("")
line2 = input("")

line1 = list(line1)
line2 = list(line2)

line1 = list(map(int, line1))
line2 = list(map(int, line2))

while len(line1) < len(line2):
    line1.insert(0, -1)

while len(line2) < len(line1):
    line2.insert(0, -1)
    
for i in range(0, len(line1)):
    if line1[i] > line2[i]:
        line2[i] = -1
    elif line2[i] > line1[i]:
        line1[i] = -1

str1 = ""
for i in line1:
    if i != -1:
        str1 += str(i)

if not str1:
    print("YODA")
else:
    print(int(str1))

str2 = ""
for i in line2:
    if i != -1:
        str2 += str(i)

if not str2:
    print("YODA")
else:
    print(int(str2))
