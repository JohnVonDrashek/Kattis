import sys

mydict = dict()

while True:
    line = input("")

    if line == "0":
        break

    tokens = line.split()

    if len(tokens) == 3 and tokens[1] == "=":
        mydict[tokens[0]] = tokens[2]
    else:
        for i in range(len(tokens) - 1, -1, -1):
            if tokens[i] in mydict:
                tokens[i] = mydict[tokens[i]]

        cont = True
        while cont:
            cont = False
            for i in range(0, len(tokens)):
                if tokens[i].isdigit() and i > 0 and not tokens[i-2].isdigit():
                    tokens[i], tokens[i-2] = tokens[i-2], tokens[i]
                    cont = True

        for i in range(len(tokens) - 1, -1, -1):
            if tokens[i] == "+":
                if tokens[i-1].isdigit() and tokens[i+1].isdigit():
                    tokens[i-1] = str(int(tokens[i-1]) + int(tokens[i+1]))
                    del tokens[i:i+2]
        for i in tokens:
            print(i, end=" ")
        print("")
