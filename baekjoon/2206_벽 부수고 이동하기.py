import sys
sys.stdin = open('2206_input.txt')
# sys.setrecursionlimit(10**6)


def bfs(x, y, cnt, bomb):
    global N, M
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = []
    q.append((x, y, cnt, bomb))
    visited[x][y] = [cnt, bomb]
    if N == 1 and M == 1: return 1
    while q:

        x, y, ncnt, nbomb = q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or ny == M: continue
            if nx < 0 or nx == N: continue
            if nx == (N - 1) and ny == (M - 1):
                return ncnt+1
            if g[nx][ny] == 1:

                if visited[x][y][1] > 0:
                    if visited[nx][ny][0] > (ncnt+1):
                        q.append((nx, ny, ncnt + 1, nbomb - 1))
                        visited[nx][ny] = [ncnt+1, nbomb-1]
                    else:
                        continue
                else:
                    continue

            else:
                if visited[x][y][1] > visited[nx][ny][1]:
                    visited[nx][ny] = [ncnt+1, visited[x][y][1]]
                    q.append((nx, ny, ncnt + 1, nbomb))

                else:
                    if visited[nx][ny][0] > (ncnt + 1):
                        visited[nx][ny] = [ncnt + 1, nbomb]
                        q.append((nx, ny, ncnt + 1, nbomb))

                    else:
                        continue

    return 0

N, M = map(int, input().split())
g = []
visited = [[[1000001, 0] for _ in range(M)] for _ in range(N)]
for _ in range(N):
    g.append(list(map(int, input())))

# for i in range(N):
#     print(g[i])

res = bfs(0, 0, 1, 1)
if res == 0:
    print(-1)
else:
    print(res)