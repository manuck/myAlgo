import sys
sys.stdin = open('17144_input.txt')

'''
공기청정기는 항상 왼쪽 열에 설치되어 있고, 크기는 두 행을 차지한다. 공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.

1초 동안 아래 적힌 일이 순서대로 일어난다.

미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
(r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
확산되는 양은 Ar,c/5이고 소수점은 버린다.
(r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
공기청정기가 작동한다.
공기청정기에서는 바람이 나온다.
위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
'''

# 미세먼지 확산 함수
def dust():
    global r, c, dx, dy
    after = [[0 for _ in range(c)]for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if g[i][j] > 4:
                div = g[i][j]//5
                for q in range(4):
                    nx = j + dx[q]
                    ny = i + dy[q]
                    if nx < 0 or nx >= c: continue
                    if ny < 0 or ny >= r: continue
                    if g[ny][nx] == -1: continue
                    after[ny][nx] += div
                    g[i][j] -= div

    for i in range(r):
        for j in range(c):
            g[i][j] += after[i][j]

# 공기정화 함수
def clean():
    global top, bottom, r, c
    # 상단(↓)
    for i in range(top-1, 0, -1):
        g[i][0] = g[i-1][0]
    # 상단(←)
    for i in range(c-1):
        g[0][i] = g[0][i+1]
    # 상단(↑)
    for i in range(top):
        g[i][c-1] = g[i+1][c-1]
    # 상단(→)
    for i in range(c-1, 1, -1):
        g[top][i] = g[top][i-1]

    # 하단(↑)
    for i in range(bottom+1, r-1):
        g[i][0] = g[i+1][0]
    # 하단(←)
    for i in range(c-1):
        g[r-1][i] = g[r-1][i+1]
    # 하단(↓)
    for i in range(r-1, bottom, -1):
        g[i][c-1] = g[i-1][c-1]
    # 하단(→)
    for i in range(c-1, 1, -1):
        g[bottom][i] = g[bottom][i-1]

    # 상단, 하단 우측 한칸 정화
    g[bottom][1] = 0
    g[top][1] = 0




r, c, t = map(int, input().split())
g = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
top, bottom = 0, 0
b = [[0]*c for _ in range(r)]
for i in range(r):
    g.append(list(map(int, input().split())))

# for i in range(r):
#     print(g[i])

for i in range(r):
    if g[i][0] == -1:
        top = i
        bottom = i + 1
        break
# print(top, bottom)

# for i in range(c-1, 0, -1):
#     print(i)

for i in range(t):
    dust()
    # print('----------확산---------------')
    # for j in range(r):
    #     print(g[j])
    clean()
    # print('-----------청소-------------')
    # for j in range(r):
    #     print(g[j])

# for i in range(r):
#     print(g[i])

res = 0
for i in range(r):
    for j in range(c):
        res += g[i][j]

print(res+2)