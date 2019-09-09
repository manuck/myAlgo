import sys
sys.stdin = open("input.txt", "r")


def DFS(v):
    visit[v] = True
    for w in G[v]:
        if not visit[w]:
            DFS(w)

    stack.append(v)


for test_case in range(1, 11):
    V, E = map(int, input().split())

    G = [[] for i in range(V + 1)]
    visit = [False] * (V + 1)
    in_degree = [0] * (V + 1)
    stack = []

    arr = list(map(int, input().split()))
    for i in range(0, E):
        u, v = arr[i * 2], arr[i * 2 + 1]
        G[u].append(v)  # 유향 그래프
        in_degree[v] += 1

    for i in range(1, V + 1):
        if in_degree[i] == 0:
            DFS(i)

    print("#%d" % test_case, end="")
    for val in stack[::-1]:
        print(" %d" % val, end="")
    print()

