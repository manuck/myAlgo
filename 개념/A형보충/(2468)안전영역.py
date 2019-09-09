
from collections import deque

def BFS(x, y, H):
    Q.append((x, y))
    visit[x][y] = H
    while len(Q) > 0:
        x, y = Q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            tx, ty = x + dx, y + dy
            if tx < 0 or tx == N or ty < 0 or ty == N: continue
            if area[tx][ty] <= H or visit[tx][ty] == H: continue
            visit[tx][ty] = H
            Q.append((tx, ty))


N = int(input())
area = []
visit = [[0] * N for _ in range(N)]

MIN, MAX = 1000, 0
for i in range(N):
    area.append(list(map(int, input().split())))
    for j in range(N):
        MAX = max(MAX, area[i][j])
        MIN = min(MIN, area[i][j])

Q = deque()
ans = 1                            # 모든 지역의 높이가 같을 경우
for H in range(MIN, MAX):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] <= H or visit[i][j] == H: continue
            cnt += 1
            BFS(i, j, H)

    ans = max(ans, cnt)

print(ans)

