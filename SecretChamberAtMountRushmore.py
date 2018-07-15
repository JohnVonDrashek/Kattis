import sys

line = input("")
m, n = line.split(" ")
m = int(m)
n = int(n)

mymap = dict()


for i in range(0, m):
    a, b = input("").split(" ")

    if not a in mymap:
        mymap[a] = a

    mymap[a] += b

    for key, val in mymap.items():
        if key in mymap[a]:
            for c in val:
                if c not in mymap[a]:
                    mymap[a] += c
for a, b in mymap.items():
    for key, val in mymap.items():
        if key in mymap[a]:
            for c in val:
                if c not in mymap[a]:
                    mymap[a] += c

for a, b in mymap.items():
    for key, val in mymap.items():
        if key in mymap[a]:
            for c in val:
                if c not in mymap[a]:
                    mymap[a] += c

for a, b in mymap.items():
    for key, val in mymap.items():
        if key in mymap[a]:
            for c in val:
                if c not in mymap[a]:
                    mymap[a] += c

for i in range(0, n):
    line = input("")
    x, y = line.split(" ")

    count = 0

    if len(x) == len(y):
        for j in range(0, len(x)):
            cont = 0
            if x[j] in mymap:
                for c in mymap[x[j]]:
                    if c == y[j] and cont == 0:
                        cont = 1
                        count += 1
            elif x[j] == y[j]:
                count += 1

    if count == len(x):
        print("yes")
    else:
        print("no")
    
    
                    
