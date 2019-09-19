import sys, time
sys.stdin = open('2573_input.txt')

start = time.time()
import copy

def bfs(x, y):
    global N, M, landcnt
    landcnt += 1
    if landcnt >= 2:
        return
    q = [[x, y]]
    visited = [[0 for _ in range(M)]for _ in range(N)]
    visited[y][x] = 1
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M: continue
            if ny < 0 or ny >= N: continue
            if visited[ny][nx] == 0 and gcopy[ny][nx] != 0:
                q.append([nx, ny])
                visited[ny][nx] = 1
                gcopy[ny][nx] = 0



N, M = map(int, input().split())
g = []
for i in range(N):
    g.append(list(map(int, input().split())))
# print(time.time()-start)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0
while True:
    # 섬의 개수
    gcopy = copy.deepcopy(g)
    mysum = 0
    # for i in range(N):
    #     mysum += sum(g[i])
    # print(mysum)

    landcnt = 0
    for i in range(1, N):
        if landcnt >= 2:
            mysum += 1
            break
        for j in range(1, M):
            if gcopy[i][j] != 0:
                mysum += 1
                bfs(j, i)
    # print(landcnt)
    if landcnt >= 2:
        break
    
    # 빙하 녹이기
    later = []
    for i in range(1, N):
        for j in range(1, M):
            if g[i][j] != 0:
                cnt = 0
                for q in range(4):
                    if (i + dy[q]) < 0 or (i + dy[q]) >= N: continue
                    if (j + dx[q]) < 0 or (j + dx[q]) >= M: continue
                    if g[i + dy[q]][j + dx[q]] == 0:
                        cnt += 1
                if cnt != 0:
                    later.append([i, j, cnt])

    if mysum == 0:
        break
    # print(later)
    # for i in range(N):
    #     print(g[i])
    for i in range(len(later)):
        g[later[i][0]][later[i][1]] -= later[i][2]
        if g[later[i][0]][later[i][1]] < 0:
            g[later[i][0]][later[i][1]] = 0
    ans += 1
    # print('-------------------------')
    # for i in range(N):
    #     print(g[i])
zxc = 0
for i in range(N):
    zxc += sum(g[i])
if zxc == 0:
    print(0)
else:
    print(ans)
print(time.time()-start)