import sys
sys.stdin = open('14889_input.txt')

import itertools

n = int(input())
g = [list(map(int, input().split()))for _ in range(n)]
a = list(range(n))
b = [0] * n
c = list(itertools.combinations(a, n//2))
ans = 9999999

for i in range(len(c)//2):
    startPower = 0
    linkPower = 0
    # 스타트 팀 구분 및 시너지 계산
    start = list(itertools.combinations(c[i], 2))
    # print(start)
    for j in range(len(start)):
        startPower += g[start[j][0]][start[j][1]]
        startPower += g[start[j][1]][start[j][0]]

    # 링크 팀 구분 및 시너지 계산
    link = list(itertools.combinations(c[-i-1], 2))
    # print(link)
    for j in range(len(link)):
        linkPower += g[link[j][0]][link[j][1]]
        linkPower += g[link[j][1]][link[j][0]]

    # 스타트 팀과 링크 팀의 최소차이 계산
    res = abs(startPower - linkPower)
    if ans > res:
        ans = res

print(ans)
