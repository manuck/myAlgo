import sys
sys.stdin = open('zxc_input.txt')


import copy, itertools

def check(x, y):    # 섬 확인
    global n, gbackup, m
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = [[x, y]]
    visit = [[0 for _ in range(m)]for _ in range(n)]
    visit[y][x] = 1
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m: continue
            if ny < 0 or ny >= n: continue
            if visit[ny][nx] == 0 and gbackup[ny][nx] == 1:
                visit[ny][nx] = 1
                gbackup[ny][nx] = 0
                q.append([nx, ny])

    return visit

def dfs(v):     # 정점의 연결되는 수 확인
    visitV[v] = 1
    # print(v)
    for w in range(len(landlist)):
        if myarray[v][w] != 0 and visitV[w] == 0:
            dfs(w)


def vs(a, b, start):        # bfs 돌면서 동,서,남,북 확인 및 다리 카운트
    global n, m
    cnt = 1000
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = [start]
    visit = [[0 for _ in range(m)]for _ in range(n)]
    visit[start[1]][start[0]] = 1
    one = 1000
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m: continue
            if ny < 0 or ny >= n: continue
            if a[ny][nx] == 1 and visit[ny][nx] == 0:
                q.append([nx, ny])
                visit[ny][nx] = 1


        # 동쪽 확인
        cnt1 = 0
        while True:
            if cnt1 + x >= m:
                break
            if cnt1 != 0:
                if g[y][x + cnt1] == 1 and b[y][x+cnt1] == 0:
                    break
            if b[y][x + cnt1] == 1:
                # if one > cnt1:
                #     one = cnt1
                if cnt > cnt1:
                    if cnt1 > 2:
                        cnt = cnt1
                state = 0
                break
            cnt1 += 1

        # 서쪽 확인
        cnt2 = 0
        while True:
            if x - cnt2 < 0:
                break
            if cnt2 != 0:
                if g[y][x - cnt2] == 1 and b[y][x - cnt2] == 0:
                    break
            if b[y][x - cnt2] == 1:
                # if one > cnt2:
                #     one = cnt2
                if cnt > cnt2:
                    if cnt2 > 2:
                        cnt = cnt2
                state = 0
                break
            cnt2 += 1

        # 남쪽 확인
        cnt3 = 0
        while True:
            if cnt3 + y >= n:
                break
            if cnt3 != 0:
                if g[y + cnt3][x] == 1 and b[y + cnt3][x] == 0:
                    break
            if b[y + cnt3][x] == 1:
                # if one > cnt3:
                #     one = cnt3
                if cnt > cnt3:
                    if cnt3 > 2:
                        cnt = cnt3
                state = 0
                break
            cnt3 += 1

        # 북쪽 활인
        state = 1
        cnt4 = 0
        while state:
            if y - cnt4 < 0:
                state = 0
                break
            if cnt4 != 0:
                if g[y - cnt4][x] == 1 and b[y - cnt4][x] == 0:
                    break
            if b[y - cnt4][x] == 1:
                # if one > cnt4:
                #     one = cnt4
                if cnt > cnt4:
                    if cnt4 > 2:
                        cnt = cnt4
                break
            cnt4 += 1
    # print('one', one, end=" ")
    # print('cnt', cnt)
    # print(start)
    # print(a, b)
    if cnt == 1000:
        return 0
    else:
        if one == 2:
            return 0
        # else:
        return cnt-1


def mst():      # 최소신장트리(프림)
    global V
    total = 0
    u = 0       #시작점을 0으로
    D[u] = 0

    for i in range(V+1):  # 가중치 최소값 찾기
        min = 9999999
        for v in range(V+1):
            if visited[v] == 0 and min > D[v]:
                min = D[v]
                u = v

        visited[u] = 1       # 방문처리
        total += myarray[landindex[u]][u]

        for v in range(V+1): #인접한 정점 업데이트
            if myarray[u][v] != 0 and visited[v] == 0 and myarray[u][v] < D[v]:
                D[v] = myarray[u][v]
                landindex[v] = u

    # print(visited)
    return total

n, m = map(int, input().split())
g = []
for i in range(n):
    g.append(list(map(int, input().split())))

landlist = []       # 섬 리스트
landstart = []      # 섬의 시작 좌표
gbackup = copy.deepcopy(g)
for i in range(n):
    for j in range(m):
        if gbackup[i][j] == 1:
            landlist.append(check(j, i))
            landstart.append([j, i])

landindex = list(range(len(landlist)))
# print(landindex)
sm = list(itertools.permutations(landindex, 2))
myarray = [[0 for _ in range(len(landlist))]for _ in range(len(landlist))]
# print(myarray)
for i in range(len(sm)):
    myarray[sm[i][1]][sm[i][0]] = vs(landlist[sm[i][0]], landlist[sm[i][1]], landstart[sm[i][0]])   # 비교할 섬 A, B, 그리고 A의 시작 좌표

for i in range(len(myarray)):
    print(myarray[i])

zxc = []    # i섬에서 j섬까지의 누적치
for i in range(len(myarray)):
    for j in range(len(myarray)):
        if myarray[i][j] != 0 and j > i:
            zxc.append([i, j, myarray[i][j]])

# print(zxc)
V, E = len(myarray)-1, len(myarray)
D = [99999] * (V + 1)
visited = [0] * (V + 1)
visitV = [0] * (V + 1)
# print(V, E)
# print(len(zxc))
sol = mst()     # 최소신장트리 (모든 정점이 연결되었다는 가정)
outsider = 0    # 연결되어있는 수
for i in range(1, len(visitV)):
    if visitV[i] == 0:
        outsider += 1
        dfs(i)
# print(len(landlist))
# print('연결', outsider)
if sol == 0 or outsider != 1 or len(zxc) < (len(landlist)-1):
    print(-1)
else:
    print(sol)
