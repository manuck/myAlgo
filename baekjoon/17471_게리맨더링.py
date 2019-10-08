import sys
sys.stdin = open('17471_input.txt')


def bfs(area, n):
    q = [area[0]]
    v = [0] * (n + 1)
    v[area[0]] = 1

    total = 0
    while q:
        i = q.pop(0)
        total += a[i]
        for j in area:
            if g[i][j] == 1 and v[j] == 0:
                q.append(j)
                v[j] = v[i] + 1
    for i in area:
        if v[i] == 0:
            return 0
    return total

import itertools
n = int(input())
a = list(map(int, input().split()))     #  1번 구역부터 N번 구역까지 순서대로 인구수
b = [list(map(int, input().split())) for _ in range(n)]     # N개의 줄에 각 구역과 인접한 구역의 정보, 첫 번째 정수는 그 구역과 인접한 구역의 수이고, 이후 인접한 구역의 번호가 주어진다

section = list(range(len(a)))
g = [[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    for j in range(1, len(b[i])):
        g[i][b[i][j]-1] = 1

ans = 9999
r = 1
for i in range(n//2):
    c = list(itertools.combinations(section, r))
    d = list(itertools.combinations(section, len(section)-r))
    r += 1

    for j in range(len(c)):

        cnt1 = 0
        cnt2 = 0
        section1 = 0
        section2 = 0
        visit = [0] * n
        A = bfs(c[j], n)
        B = bfs(d[~j], n)

        if A * B != 0:
            if ans > abs(A-B):
                ans = abs(A-B)

if ans == 9999:
    print(-1)
else:
    print(ans)
