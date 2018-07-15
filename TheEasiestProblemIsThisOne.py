import sys

x = int(input(""))

while x != 0:
    string = str(x)
    sumo = 0
    
    
    for c in string:
        sumo += int(c)

    cont = 1
    m = 10
    tempnum = 0

    while cont == 1:
        mytemp = 0
        m += 1
        tempnum = x * m
        tempnumstr = str(tempnum)
        
        for c in tempnumstr:
            mytemp += int(c)

        if mytemp == sumo:
            cont = 0

        
    print(m)
        
    x = int(input(""))
