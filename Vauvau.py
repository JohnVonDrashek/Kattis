import sys

line1 = input("")
line2 = input("")

a,b,c,d = line1.split(" ")
a = int(a)
b = int(b)
c = int(c)
d = int(d)

dog1cycle = a + b
dog2cycle = c + d

for i in line2.split(" "):
    p = int(i)
    numofdogs = 0
    
    if ((p-1) % (dog1cycle)) + 1 <= a:
        numofdogs += 1
    if ((p-1) % (dog2cycle)) + 1 <= c:
        numofdogs += 1

    if numofdogs == 0:
        print("none")
    if numofdogs == 1:
        print("one")
    if numofdogs == 2:
        print("both")
