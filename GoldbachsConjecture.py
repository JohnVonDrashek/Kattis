import sys
from math import sqrt
from itertools import count, islice

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    return prime

            
n = int(input())
isPrime = SieveOfEratosthenes(32000)

for i in range(n):
    x = int(input())
    reps = 0
    sums = []

    for j in range(2, int(x/2) + 1):
        a = j
        b = x - j

        if isPrime[a] and isPrime[b]:
            reps += 1
            sums.append(str(a) + "+" + str(b))

    print(str(x) + " has " + str(reps) + " representation(s)")
    for j in sums:
        print(j)

    print()
