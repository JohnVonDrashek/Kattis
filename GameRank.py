import sys

line = input("")

wins = 0
losses = 0
streak = 0
stars = 0
rank = 25
islegend = False

for i in line:
    if rank == 0:
        islegend = True

    if i == "W":
        stars += 1
        streak += 1

        if 6 <= rank <= 25 and streak >= 3:
            stars += 1
    
        if 21 <= rank <= 25 and stars > 2:
            rank -= 1
            stars -= 2
        elif 16 <= rank <= 20 and stars > 3:
            rank -= 1
            stars -= 3
        elif 11 <= rank <= 15 and stars > 4:
            rank -= 1
            stars -= 4
        elif 1 <= rank <= 10 and stars > 5:
            rank -= 1
            stars -= 5
    else:
        streak = 0
        if 1 <= rank <= 20:
            stars -= 1

        if stars < 0 and rank >= 1 and rank <= 20:
            if rank == 20:
                stars = 0
                continue
            rank += 1
            if rank <= 20 and rank >= 16:
                stars = 2
            elif rank <= 15 and rank >= 11:
                stars = 3
            elif rank <= 10 and rank >= 1:
                stars = 4
        
if islegend or rank == 0:
    print("Legend")
else:
    print(rank)

    
