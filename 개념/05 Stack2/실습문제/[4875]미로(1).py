# 스택을 사용해서 반복으로 구현
import sys
sys.stdin = open("4875.txt", "r")


sx = sy = ex = ey = 0

def DFS(x, y, ex, ey):
    visit = [[False for _ in range(N)] for _ in range(N)]
    S = []
    visit[x][y] = True
    S.append((x, y))

    while len(S) > 0:
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tx, ty = x + dx, y + dy
            if tx < 0 or tx == N or ty < 0 or ty == N:
                continue
            if visit[tx][ty] or maze[tx][ty] == '1':
                continue
            visit[tx][ty] = True
            S.append((x, y))
            x, y = tx, ty
            break
        else:
            x, y = S.pop()

    return visit[ex][ey]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    maze = []
    for i in range(N):
        maze.append(input())
        for j in range(N):
            if maze[i][j] == '2':
                sx, sy = i, j
            if maze[i][j] == '3':
                ex, ey = i, j

    print("#%d %d" % (test_case, DFS(sx, sy, ex, ey)))

