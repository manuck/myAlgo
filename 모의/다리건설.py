import sys
sys.stdin = open('다리건설_input.txt')

import copy, itertools

def check(x, y):
    global n, gbackup
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
            if visit[ny][nx] == 0 and gbackup[ny][nx] == 1:
                visit[ny][nx] = 1
                gbackup[ny][nx] = 0
                q.append([nx, ny])

    return visit


def vs(a, b, start):
    global n
    cnt = 1000
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = [start]
    visit = [[0 for _ in range(n)]for _ in range(n)]
    visit[start[1]][start[0]] = 1
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n: continue
            if ny < 0 or ny >= n: continue
            if a[ny][nx] == 1 and visit[ny][nx] == 0:
                q.append([nx, ny])
                visit[ny][nx] = 1

        state = 1
        cnt1 = 0
        while state:
            if cnt1 + x >= n:
                state = 0
                break
            if b[y][x + cnt1] == 1:
                if cnt > cnt1:
                    cnt = cnt1
                state = 0
                break
            cnt1 += 1

        state = 1
        cnt2 = 0
        while state:
            if x - cnt2 < 0:
                state = 0
                break
            if b[y][x - cnt2] == 1:
                if cnt > cnt2:
                    cnt = cnt2
                state = 0
                break
            cnt2 += 1

        state = 1
        cnt3 = 0
        while state:
            if cnt3 + y >= n:
                state = 0
                break
            if b[y + cnt3][x] == 1:
                if cnt > cnt3:
                    cnt = cnt3
                state = 0
                break
            cnt3 += 1

        state = 1
        cnt4 = 0
        while state:
            if y - cnt4 < 0:
                state = 0
                break
            if b[y - cnt4][x] == 1:
                if cnt > cnt4:
                    cnt = cnt4
                state = 0
                break
            cnt4 += 1
    if cnt == 1000:
        return 0
    else:
        return cnt-1


def mst():
    global V
    total = 0
    u = 0       #시작점을 0으로
    D[u] = 0

    for i in range(V+1):  # 가중치 최소값 찾기
        min = 987654321
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

    return total



t = int(input())

for case in range(t):
    n = int(input())
    g = []
    for i in range(n):
        g.append(list(map(int, input().split())))

    landlist = []
    landstart = []
    gbackup = copy.deepcopy(g)
    for i in range(n):
        for j in range(n):
            if gbackup[i][j] == 1:
                landlist.append(check(j, i))
                landstart.append([j, i])

    # print(landlist)
    # for i in range(len(landlist)):
    #     for j in range(n):
    #         print(landlist[i][j])
    #     print()
    landindex = list(range(len(landlist)))
    # print(landindex)
    sm = list(itertools.permutations(landindex, 2))
    myarray = [[0 for _ in range(len(landlist))]for _ in range(len(landlist))]
    # print(myarray)
    for i in range(len(sm)):
        myarray[sm[i][1]][sm[i][0]] = vs(landlist[sm[i][0]], landlist[sm[i][1]], landstart[sm[i][0]])

    print(myarray)
    zxc = []
    for i in range(len(myarray)):
        for j in range(len(myarray)):
            if myarray[i][j] != 0 and j > i:
                zxc.append([i, j, myarray[i][j]])

    print(zxc)
    V, E = len(myarray)-1, len(myarray)
    adj = [[0] * (V + 1) for _ in range(V + 1)] # myarray
    D = [987654321] * (V + 1)
    PI = list(range(V + 1))     # landindex
    visited = [0] * (V + 1)

    print(mst())

