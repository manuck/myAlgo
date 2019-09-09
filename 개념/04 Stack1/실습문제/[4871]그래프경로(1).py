import sys
sys.stdin = open("input.txt", "r")


def DFS(v):
    visit[v] = True

    for w in G[v]:
        if not visit[w]:
            DFS(w)


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    G = [[] for i in range(V + 1)]
    visit = [False] * (V + 1)

    for i in range(E):
        u, v = map(int, input().split())
        G[u].append(v)              # 유향 그래프

    start, target = map(int, input().split())

    DFS(start)
        
    print("#%d %d" % (test_case, visit[target]))

