import sys
from collections import deque

n, m = list(map(int, input().split(" ")))

m_map = []

m_map.append([0] * (m+2))

for i in range(n):
    m_map.append([0] + list(map(int, list(input()))) + [0])
m_map.append([0] * (m+2))
def in_bounds(x, y):
    if x >= 0 and x < n+2 and y >= 0 and y < m+2:
        return True
    else:
        return False

traversed = dict()

q = deque([(0,0)])
coast = 0
while q:
    x, y = q.pop()

    if in_bounds(x,y) and m_map[x][y] == 0:
        m_map[x][y] = 2
        for mx, my in [(x+1,y),(x-1,y), (x,y+1), (x,y-1)]:
            if not in_bounds(mx, my):
                continue
            if m_map[mx][my] == 2:
                continue
            if m_map[mx][my] == 1:
                coast += 1
                continue
            if m_map[mx][my] == 0:
                q.append([mx,my])
                continue

print(coast)
