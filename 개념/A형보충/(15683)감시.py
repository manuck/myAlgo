dx = [-1, 1, 0, 0]  # 상(0), 하(1), 좌(2), 우(3)
dy = [0, 0, -1, 1]
dir = [ [[0]],
        [[0], [1], [2], [3]],                           # (상), (하), (좌), (우)
        [[0, 1], [2, 3]],                               # (상, 하), (좌, 우)
        [[0, 2], [0, 3], [1, 2], [1, 3]],               # (상, 좌), (상, 우), (하, 좌), (하, 우)
        [[0, 2, 3], [1, 2, 3], [0, 1, 2], [0, 1, 3]],   # (상, 좌, 우), (하, 좌, 우), (상, 하, 좌), (상, 하, 우)
        [[0, 1, 2, 3]]                                  # (상, 하, 좌, 우)
       ]
# --------------------------------------------------

def setValue(x, y, lst, val):
    for d in lst:
        tx, ty = x + dx[d], y + dy[d]
        while 0 <= tx < N and 0 <= ty < M and MAP[tx][ty] != 6:
            visit[tx][ty] += val
            tx, ty = tx + dx[d], ty + dy[d]

def backtrack(k, n):
    global MIN
    if k == n:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if MAP[i][j] == 0 and visit[i][j] == 0:
                    cnt += 1
        MIN = min(MIN, cnt)
    else:
        x, y, t = cctv[k]
        for lst in dir[t]:
            setValue(x, y, lst, 1)

            backtrack(k + 1, n)

            setValue(x, y, lst, -1)

# --------------------------------------------------

N, M = map(int, input().split())
MAP = []
cctv = []
for i in range(N):
    MAP.append(list(map(int, input().split())))
    for j in range(M):
        if 0 < MAP[i][j] < 6:
            cctv.append((i, j, MAP[i][j]))

visit = [[0] * M for _ in range(N)]
MIN = N * M

backtrack(0, len(cctv))
print(MIN)
