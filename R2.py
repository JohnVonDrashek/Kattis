import sys

t = input("")

r, s = t.split(" ")

r = int(r)
s = int(s)

s *= 2
s -= r

print(s)
