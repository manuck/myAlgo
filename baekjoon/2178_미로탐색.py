import sys
sys.stdin = open('2178_input.txt')


def bfs(x, y, cnt):
    global N, M
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = []
    q.append((x, y, cnt))
    visited[x][y] = 1
    while len(q) != 0:
        x, y, ncnt = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or ny == M: continue
            if nx < 0 or nx == N: continue
            if nx == (N-1) and ny == (M-1):
                return ncnt
            elif g[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny, ncnt+1))
                visited[nx][ny] = 1
                # print('-------------------------------')
                # print('ncnt: ', ncnt)
                # for w in range(N):
                #     print(visited[w])
    return 0


N, M = map(int, input().split())
g = []
visited = [[0 for _ in range(M)]for _ in range(N)]
for i in range(N):
    g.append(list(map(int, input())))

# for i in range(N):
#     print(g[i])
# print(visited)

res = bfs(0, 0, 2)
print(res)