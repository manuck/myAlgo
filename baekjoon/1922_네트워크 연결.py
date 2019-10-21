import sys
sys.stdin = open('1922_input.txt')


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
m = int(input())

a = []
b = list(range(n+1))
for i in range(m):
    a.append(list(map(int, input().split())))
ans = 0
cnt = 0
# print(a)
a.sort(key=lambda x: x[2])
# print(a)
# print(b)
mst()
print(ans)