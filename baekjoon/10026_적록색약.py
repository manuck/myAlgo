import sys
sys.stdin = open('10026_input.txt')

'''
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

'''

def check1(x, y, a):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = [[x, y]]
    visit = [[0 for _ in range(n)]for _ in range(n)]
    visit[y][x] = 1
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n: continue
            if ny < 0 or ny >= n: continue
            if visit[ny][nx] == 0 and g[ny][nx] == a:
                visit[ny][nx] = 1
                g[ny][nx] = 0
                q.append([nx, ny])
    return visit

def check2(x, y, a):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = [[x, y]]
    visit = [[0 for _ in range(n)]for _ in range(n)]
    visit[y][x] = 1
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n: continue
            if ny < 0 or ny >= n: continue
            if visit[ny][nx] == 0 and color[ny][nx] == a:
                visit[ny][nx] = 1
                color[ny][nx] = 0
                q.append([nx, ny])
    return visit

n = int(input())
g = [list(input()) for _ in range(n)]
color = [[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    for j in range(n):
        if g[i][j] == 'R':
            color[i][j] = 'G'
        else:
            color[i][j] = g[i][j]

ans1 = 0
ans2 = 0
for i in range(n):
    for j in range(n):
        if g[i][j] != 0:
            check1(j, i, g[i][j])
            ans1 += 1

for i in range(n):
    for j in range(n):
        if color[i][j] != 0:
            check2(j, i, color[i][j])
            ans2 += 1

print(ans1, ans2)
