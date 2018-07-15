import sys

left = []
right = []

N, k = list(map(int, input().split(" ")))

for i in range(0, N):
    a, b = list(map(int, input().split(" ")))
    left.append(a)
    right.append(b)

catch = input("")

while k > 0:
    val = 10000
    posx = -1
    posy = -1
    
    for i in range(0, N):
        if left[i] != -1 and left[i] <= val and right[max(i-1,0)] != -1 and right[i] != -1 and right[min(i+1, N-1)] != -1:
            val = left[i]
            posx = i
            posy = 1
        if right[i] != -1 and right[i] <= val and left[max(i-1,0)] != -1 and left[i] != -1 and left[min(i+1, N-1)] != -1:
            val = right[i]
            posx = i
            posy = 2

    k -= 1
    if posy == 1:
        left[posx] = -1
    else:
        right[posx] = -1

total = 0

for i in left:
    if i != -1:
        total += i

for i in right:
    if i != -1:
        total += i

print(total)
    
