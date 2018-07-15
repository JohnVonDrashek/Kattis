import sys

l = int(input(""))
d = int(input(""))
x = int(input(""))

for p in range(l, d+1):
    mysum = 0
    st = str(p)

    for s in st:
        mysum += int(s)
        
    if mysum == x:
        print(p)
        break

for p in range(d, l-1, -1):
    mysum = 0
    st = str(p)

    for s in st:
        mysum += int(s)
        
    if mysum == x:
        print(p)
        break
