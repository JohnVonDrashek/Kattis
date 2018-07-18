import sys
import math

m, n, t = list(map(int, input("").split(" ")))

result = 0

def factorMe(n):
    cur = n
    total = 1
    while cur != 0:
        total *= cur
        cur -= 1
        if total > m:
            return m + 1
    return total

def powerMe(a, b):
    total = 1

    for i in range(b):
        total *= a
        if total > m:
            return m + 1
    return total

if t == 1:
    result = factorMe(n)    
elif t == 2:
    result = powerMe(2, n)
elif t == 3:
    result = powerMe(n, 4)
elif t == 4:
    result = powerMe(n, 3)
elif t == 5:
    result = powerMe(n, 2)
elif t == 6:
    result = n * math.log(n, 2)
elif t == 7:
    result = n


if result <= m:
    print("AC")
else:
    print("TLE")
