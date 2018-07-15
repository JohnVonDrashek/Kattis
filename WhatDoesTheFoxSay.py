import sys

t = int(input(""))

for i in range(0,t):
    test_case = input("")

    words = []

    i = input("")
    while i != "what does the fox say?":
        temp_words = i.split(" ")
        words.append(temp_words[2])
        i = input("")
        
    for word in test_case.split(" "):
        if word not in words:
            print(word, end=" ")
        print("")
