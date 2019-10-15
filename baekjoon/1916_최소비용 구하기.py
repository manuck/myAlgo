import sys
sys.stdin = open('1916_input.txt')


def bfs():
    visit = [999999999] * (n+1)
    visit[start] = 0

    q = [(start, 0)]
    while q:
        # print(q)
        now, cost_sum = q.pop(0)      # now = 현재, cost_sum = 누적값
        for i, j in g[now]:
            # print(visit)
            # print('현재', i)
            # print('합', cost_sum + j)
            if cost_sum + j < visit[i]:
                visit[i] = cost_sum + j
                q.append((i, cost_sum + j))
    # print(visit)
    return visit[end]


n = int(input())    # 도시의 개수
m = int(input())    # 버스의 개수
g = [[] for _ in range(n+1)]

for i in range(m):
    s, e, cost = map(int, input().split())
    g[s].append((e, cost))

start, end = map(int, input().split())
# print(g)
ans = bfs()
print(ans)

