import sys

n, m = map(int, input().split(" "))

conns = dict()

for i in range(0, m):
    a, b = map(int, input().split(" "))

    if a in conns:
        conns[a].append(b)
    else:
        conns[a] = [b]

    if b in conns:
        conns[a].append(b)
    else:
        conns[a] = [b]

travelled = [False] * n
nconns = dict()

while False in travelled:
    length = m

    for key in conns:
        length = min(length, len(conns[key]))

    mykey = -1
    for key in conns:
        if len(conns[key]) == length:
            mykey = key
            for i in conns[key]:
                if travelled[i] == False:
                    travelled[i] = True
                    if key in nconns:
                        nconns[key].append(i)
                    else:
                        nconns[key] = [i]
                if travelled[key] == False:
                    travelled[key] = True
                    if key in nconns:
                        nconns[key].append(i)
                    else:
                        nconns[key] = [i]
                        
    conns.pop(mykey, None)

for key, value in nconns.items():
    print(key)
    print(value)
