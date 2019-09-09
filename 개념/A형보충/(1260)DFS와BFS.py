from collections import deque

def DFS(v):
    visit[v] = True
    ans.append(v)

    for w in G[v]:
        if not visit[w]:
            DFS(w)

def BFS(s):
    visit[s] = True
    Q = deque()
    Q.append(s)
    ans.append(s)

    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                Q.append(w)
                ans.append(w)
                visit[w] = True


N, M, s = map(int, input().split())
G = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for lst in G:
    lst.sort()

ans = []
visit = [False] * (N + 1)
DFS(s)
print(' '.join(map(str, ans)))

ans = []
visit = [False] * (N + 1)
BFS(s)
print(' '.join(map(str, ans)))