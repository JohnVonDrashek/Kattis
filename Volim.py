import sys

players = 8
maxtime = 210
k = int(input(""))
n = int(input(""))

for x in range(0, n):
    myline = input("")
    time, value = myline.split(" ")
    time = int(time)

    maxtime -= time

    if maxtime <= 0:
        break
    
    if value == "T":
        k += 1
        if k > players:
            k = 1

print(k)
