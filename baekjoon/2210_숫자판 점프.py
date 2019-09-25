import sys
sys.stdin = open('2210_input.txt')


def dfs(x, y, cnt, tmp):
    if cnt == 6:
        myjoin = ''.join(tmp)
        if myjoin not in ans:
            ans.append(myjoin)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 5: continue
            if ny < 0 or ny >= 5: continue

            tmp.append(g[nx][ny])
            dfs(nx, ny, cnt+1, tmp)
            tmp.pop()

g = [list(map(str, input().split())) for _ in range(5)]

ans = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for i in range(5):
    for j in range(5):
        tmp = [g[i][j]]
        dfs(i, j, 1, tmp)

# print(ans)
print(len(ans))
