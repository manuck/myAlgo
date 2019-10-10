import sys
sys.stdin = open('2644_input.txt')


def bfs(v):
    q = [v]
    visit = [0] * (n+1)
    dep = 0
    while q:
        # print()
        # print('visit', visit)
        # print('q', q)
        dep += 1
        for _ in range(len(q)):
            # print(q)
            v = q.pop(0)
            if v == end:
                return dep - 1
            for i in g[v]:
                if not visit[i]:
                    visit[i] = 1
                    q.append(i)


n = int(input())    # 사람의 수
start, end = map(int, input().split())  # 두 사람의 번호
m = int(input())    # 관계의 수
g = [[] for _ in range(n+1)]
# g = [[0 for _ in range(n+1)]for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# for i in range(n+1):
# print(g)
ans = bfs(start)
if ans == None:
    print(-1)
else:
    print(ans)