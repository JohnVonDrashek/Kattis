import sys
from math import sqrt
from functools import reduce

def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

for line in sys.stdin:
    num = int(line)
    factor = list(factors(num))
    factor.remove(num)
    
    mysum = sum(factor)

    if mysum == num:
        print(str(num) + " perfect")
    elif num - 2 <= mysum <= num + 2:
        print(str(num) + " almost perfect")
    else:
        print(str(num) + " not perfect")

    
