import sys

board = []

for i in range(8):
    board.append(list(input("")))

queens = 0
invalid = False
for i in range(8):
    for j in range(8):
        if board[i][j] == "*":
            queens += 1
            for k in range(i+1, 8):
                if board[k][j] == "*":
                    invalid = True
                    break
            for k in range(j+1, 8):
                if board[i][k] == "*":
                    invalid = True
                    break
            add = 1
            while add + i < 8 and add + j < 8:
                if board[i+add][j+add] == "*":
                    invalid = True
                    break
                add += 1
            
            sub = -1
            while i - sub < 8 and j + sub >= 0:
                if board[i-sub][j+sub] == "*":
                    invalid = True
                    break
                sub -= 1
            


if invalid or queens < 8 or queens > 8:
    print("invalid")
else:
    print("valid")
