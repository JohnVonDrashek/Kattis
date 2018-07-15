import sys

mymap = {}
mymap[0] = "zero"
mymap[1] = "one"
mymap[2] = "two"
mymap[3] = "three"
mymap[4] = "four"
mymap[5] = "five"
mymap[6] = "six"
mymap[7] = "seven"
mymap[8] = "eight"
mymap[9] = "nine"
mymap[10] = "ten"
mymap[11] = "eleven"
mymap[12] = "twelve"
mymap[13] = "thirteen"
mymap[14] = "fourteen"
mymap[15] = "fifteen"
mymap[16] = "sixteen"
mymap[17] = "seventeen"
mymap[18] = "eighteen"
mymap[19] = "nineteen"
mymap[20] = "twenty"
mymap[30] = "thirty"
mymap[40] = "forty"
mymap[50] = "fifty"
mymap[60] = "sixty"
mymap[70] = "seventy"
mymap[80] = "eighty"
mymap[90] = "ninety"

line = input("")

while True:
    line = line.split(" ")

    revised = ""

    for word in line:
        if word.isdigit():
            num = int(word)

            firstnum = num - (num % 10)
            remainder = num % 10
            
            if num <= 19:
                revised += mymap[num] + " "
            else:
                revised += mymap[firstnum]
                if remainder > 0:
                    revised += "-" + mymap[remainder]
                revised += " "
        else:
            revised += word + " "

    print(revised.capitalize())
    try:
        line = input("")
    except EOFError:
        break
