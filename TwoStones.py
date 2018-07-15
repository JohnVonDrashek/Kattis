import sys

stones = int(input(""))
winner = stones % 2

if winner == 1:
    print("Alice")
else:
    print("Bob")
