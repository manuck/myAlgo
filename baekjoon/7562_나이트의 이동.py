import sys
sys.stdin = open('7562_input.txt')

'''
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
'''

def bfs(x, y, cnt):
    global n, visited
    dx = [1, -1, 2, -2, 1, -1, 2, -2]
    dy = [2, 2, 1, 1, -2, -2, -1, -1]
    q = []
    q.append((x, y, cnt))
    visited[y][x] = 1
    while len(q) != 0:
        x, y, cnt = q.pop(0)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or ny >= n: continue
            if nx < 0 or nx >= n: continue
            if nx == ex and ny == ey:
                return cnt
            elif a[ny][nx] == 0 and visited[ny][nx] == 0:
                q.append((nx, ny, cnt+1))
                visited[ny][nx] = 1

    return cnt

t = int(input())

for case in range(t):
    n = int(input())
    a = [[0 for _ in range(n+1)]for _ in range(n+1)]
    visited = [[0 for _ in range(n+1)]for _ in range(n+1)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    cnt = 1
    # print(sx, sy, ex, ey)
    # print(a)
    if sx == ex and ex == ey:
        print(0)
    else:
        res = bfs(sx, sy, cnt)
        print(res)