from collections import deque

N, M = map(int, input().split())

maze = [input() for _ in range(N)]
D = [[[0, 0] for _ in range(M)] for _ in range(N)]


D[0][0][0] = 1
Q = deque()
Q.append((0, 0, 0))         # (x, y, w), w = 벽통과 유무

ans = 0
while Q:
    x, y, w = Q.popleft()
    if x == N - 1 and y == M - 1:
        ans = D[x][y][w]
        break

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        tx, ty = x + dx, y + dy

        if tx < 0 or tx == N or ty < 0 or ty == M: continue

        if D[tx][ty][w]:     # 길
            continue
        if maze[tx][ty] == '0':
            D[tx][ty][w] = D[x][y][w] + 1
            Q.append((tx, ty, w))
        elif w == 0:                # 벽
            D[tx][ty][1] = D[x][y][w] + 1
            Q.append((tx, ty, 1))
else:
    ans = -1

print(ans)