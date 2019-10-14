import sys
sys.stdin = open("15684_input.txt")


def dfs(r, cnt):
    global ans
    for i in range(h + 2):
        print(g[i])
    print()
    if cnt == min_cnt:
        if check():
            ans = cnt
        return
    for i in range(r, h+1):
        for j in range(1, n):
            if not g[i][j] + g[i][j-1] + g[i][j+1]:
                g[i][j] = 1
                dfs(i, cnt+1)
                g[i][j] = 0

def check():
    for j in range(1, n+1):
        t = j
        for i in range(1, h+1):
            if g[i][t]:
                t += 1
            elif g[i][t-1]:
                t -= 1
        if t != j:
            return False
    return True

n, m, h = map(int, input().split())     # n = 세로선, m = 가로선, h = 세로선마다 가로선을 놓을 수 있는 위치의 개수
g = [[0] * (n+1) for _ in range(h+2)]
ans = 9999
for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1

for min_cnt in range(4):
    dfs(1, 0)
    if ans != 9999:
        print(ans)
        break
else:
    print(-1)