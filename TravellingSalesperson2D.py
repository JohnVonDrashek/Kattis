import sys
import math

n = int(input(""))
tourx = [None] * n
toury = [None] * n

for i in range(0, n):
    line = input("")
    x, y = line.split(" ")
    tourx[i] = float(x)
    toury[i] = float(y)

tour = [None] * n
used = [None] * n
tour[0] = 0
used[0] = 1

for i in range(1, n):
    best = -1
    bestx = 1000000
    besty = 1000000
    for j in range(0, n):
        if used[j] != 1 and (best == -1 or math.hypot(tourx[i-1] - tourx[j], toury[i-1] - toury[j]) < math.hypot(tourx[i-1] - bestx, toury[i-1] - besty)):
            best = j
            bestx = tourx[j]
            besty = toury[j]
    tour[i] = best
    used[best] = 1

for i in range(0, n):
    print(tour[i])
    
