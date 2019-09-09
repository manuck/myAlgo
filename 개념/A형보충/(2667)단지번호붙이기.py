diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def DFS(x, y):
    visit[x][y] = True
    ret = 1
    for dx, dy in diff:
        tx, ty = x + dx, y + dy
        if tx < 0 or tx == N or ty < 0 or ty == N: continue
        if danji[tx][ty] == '0' or visit[tx][ty]: continue
        ret += DFS(tx, ty)
    return ret

N = int(input())

visit = [[False for _ in range(N)] for _ in range(N)]
danji = [input() for _ in range(N)]

cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if danji[i][j] == '1' and not visit[i][j]:
            result.append(DFS(i, j))
            cnt += 1

print(cnt)
result.sort()
print(*result)
