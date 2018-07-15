import sys

line = input()

b, k, g = map(int, line.split(" "))

days = 0

while b > 1:
    days += 1
    b -= int(k / g)

print(days)
    
