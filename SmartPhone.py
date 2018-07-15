import sys

T = int(input(""))

for i in range(0, T):
    wanted = input("")
    myword = input("")
    sug = []
    sug.append(input(""))
    sug.append(input(""))
    sug.append(input(""))

    finalpress = 0
    keypresses = 0

    finished = False
    while not myword == wanted and not finished:
        if wanted.startswith(myword) or len(myword) == 0:
            keypresses += len(wanted) - len(myword)
            finished = True
        else:
             myword = myword[:-1]
             keypresses += 1

    finalpress = keypresses
    
    keypresses = 0

    
    for word in sug:
        finished = False
        while not word == wanted and not finished:
            if wanted.startswith(word) or len(word) == 0:
                keypresses += len(wanted) - len(word)
                finished = True
            else:
                word = word[:-1]
                keypresses += 1

        finalpress = min(finalpress, keypresses + 1)
            
        keypresses = 0

    print(finalpress)
