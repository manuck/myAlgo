import sys
sys.stdin = open('16398_input.txt')


def find(x):
    if x != b[x]:
        b[x] = find(b[x])
    return b[x]

def mst():
    global ans, cnt
    for a1, a2, a3 in a:
        one = find(a1)
        two = find(a2)
        if one != two:
            b[one] = two
            ans += a3
            cnt += 1
        if cnt == n-1:
            break


n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

a = []
b = list(range(n))
for i in range(n):
    for j in range(n):
        if i < j:
            a.append([i, j, g[i][j]])

ans = 0
cnt = 0
a.sort(key=lambda x: x[2])
mst()
print(ans)