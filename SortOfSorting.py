import sys

n = int(input(""))
count = 0

while n != 0:
    if count > 0:
        print("")
    else:
        count = 1
        
    arr = []
    for i in range(n):
        arr.append(input())

    arr = sorted(arr, key=lambda x:x[:2])

    for i in range(0,n):
        print(arr[i])
    
    n = int(input(""))
