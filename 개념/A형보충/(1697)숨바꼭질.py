from collections import deque

N, K = map(int, input().split())
visit = [False] * 100001
Q = deque()
Q.append((N, 0))
visit[N] = True

ans = 0
while len(Q):
    x, t = Q.popleft()
    if x == K:
        ans = t
        break
    if x - 1 >= 0 and not visit[x - 1]:
        Q.append((x - 1, t + 1))
        visit[x - 1] = True
    if x + 1 <= 100000 and not visit[x + 1]:
        Q.append((x + 1, t + 1))
        visit[x + 1] = True
    if x << 1 <= 100000 and not visit[x << 1]:
        Q.append((x << 1, t + 1))
        visit[x << 1] = True

print(ans)