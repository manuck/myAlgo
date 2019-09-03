import sys
import collections
sys.setrecursionlimit(10000)

sys.stdin = open('15686_input.txt')

def comb(n, r, q):
    global liveC, C, M, visited2
    if r == 0:
        # print(T[:M])
        # print('---------------------')
        visited2 = [[9999 for _ in range(N)] for _ in range(N)]
        for i in T[:M]:
            bfs(C[i][0], C[i][1], 0)

    elif n < r:
        return
    else:
        T[r-1] = A[n-1]
        comb(n-1, r-1, q)
        comb(n-1, r, q)


def bfs(x, y, cnt):
    global N, M, sol, res
    visited1 = [[0 for _ in range(N)] for _ in range(N)]

    res = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = collections.deque([])
    q.append((x, y, cnt))
    visited1[y][x] = 1
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N: continue
            if ny < 0 or ny >= N: continue
            if visited1[ny][nx] == 0 and visited2[ny][nx] > cnt:
                q.append((nx, ny, cnt+1))
                visited2[ny][nx] = cnt + 1
                visited1[ny][nx] = 1
    # for i in range(N):
    #     print(visited2[i])
    for i in range(len(Home)):
        res += visited2[Home[i][1]][Home[i][0]]
    # print(res)
    if sol > res:
        sol = res
    return 0


N, M = map(int, input().split())
g = []
visited2 = [[9999 for _ in range(N)] for _ in range(N)]
for i in range(N):
    g.append(list(map(int, input().split())))

# for i in range(N):
#     print(g[i])

C = []  # 치킨집
Home = []   # 집
for i in range(N):
    for j in range(N):
        if g[i][j] == 2:
            C.append((j, i))
        elif g[i][j] == 1:
            Home.append((j, i))

sol = 9999999999

# print(C)
A = list(range(len(C)))
# print(A)
T = [0] * len(C)
liveC = []
comb(len(C), M, M)

print(sol)



''' 진짜 좋은 생각
from itertools import combinations as cb
N,M = map(int,input().split())
A = []
B = []
for j in range(N):
	for i,k in enumerate(map(int,input().split())):
		if k == 1: B.append((i,j))
		if k == 2: A.append((i,j))
ans = 10**9
for C in cb(A,M):
    D = [10**9]*len(B)
    for i in range(len(B)):
        x1,y1 = B[i]
        for x2,y2 in C:
            D[i] = min(D[i],abs(x1-x2)+abs(y1-y2))
    ans = min(ans,sum(D))
print(ans)
'''