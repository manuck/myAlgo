import sys
sys.stdin = open('1987_input.txt')

'''
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.
'''
from collections import deque

def bfs():
    global r, c
    q = deque()
    q.append([0, 0, g[0][0]])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # al = [g[0][0]]
    cnt = 1
    while q:
        x, y, s = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= c: continue
            if ny < 0 or ny >= r: continue
            if g[ny][nx] in s:
                continue

            cnt = max(cnt, len(s) + 1)
            q.append((nx, ny, s+g[ny][nx]))
    return cnt

r, c = map(int, input().split())
g = []
for i in range(r):
    g.append(list(input()))

res = bfs()

print(res)
