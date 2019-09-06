import sys
sys.stdin = open('15683_input.txt')


import copy
def update(dir, cctv):
    # print(cctv)
    global n, m
    z = dir % 4

    # 동
    if z == 0:
        for i in range(cctv[0]+1, m):
            if g[cctv[1]][i] == 6: break
            g[cctv[1]][i] = -1
    # 북
    if z == 1:
        for i in range(cctv[1]-1, -1, -1):
            if g[i][cctv[0]] == 6: break
            g[i][cctv[0]] = -1
    # 서
    if z == 2:
        for i in range(cctv[0]-1, -1, -1):
            if g[cctv[1]][i] == 6: break
            g[cctv[1]][i] = -1
    # 남
    if z == 3:
        for i in range(cctv[1]+1, n):
            if g[i][cctv[0]] == 6: break
            g[i][cctv[0]] = -1


def dfs(index):
    global cctv, res, g, n, m
    if index == len(cctv):
        print('=================================')
        for j in range(n):
            print(g[j])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if g[i][j] == 0:
                    cnt += 1

        if res > cnt:
            res = cnt
        return
    # cctv가 볼 수 있는 방법 가지수 만큼 반복
    for i in range(cctv_look[cctv[index]-1]):
        backup = copy.deepcopy(g)       # 백업

        if cctv[index]-1 == 0:      # cctv 1번
            update(i, cctvLocation[index])

        if cctv[index]-1 == 1:      # cctv 2번
            update(i, cctvLocation[index])
            update(i + 2, cctvLocation[index])

        if cctv[index]-1 == 2:      # cctv 3번
            update(i, cctvLocation[index])
            update(i + 1, cctvLocation[index])

        if cctv[index]-1 == 3:      # cctv 4번
            update(i, cctvLocation[index])
            update(i+1, cctvLocation[index])
            update(i+2, cctvLocation[index])

        if cctv[index]-1 == 4:      # cctv 5번
            update(i, cctvLocation[index])
            update(i+1, cctvLocation[index])
            update(i+2, cctvLocation[index])
            update(i+3, cctvLocation[index])
        dfs(index+1)
        g = copy.deepcopy(backup)       # 복귀

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

cctv = []
cctvLocation = []
cctv_look = [4, 2, 4, 4, 1]
for i in range(n):
    for j in range(m):
        if g[i][j] != 0 and g[i][j] != 6:
            cctv.append(g[i][j])
            cctvLocation.append([j, i])
# print(cctv)
# print(cctvLocation)

res = 1000
dfs(0)
print(res)
