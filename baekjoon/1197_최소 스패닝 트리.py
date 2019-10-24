import sys
sys.stdin = open('1197_input.txt')


def find(x):
    if x != b[x]:
        b[x] = find(b[x])
    return x

def mst():
    global ans, cnt
    for a1, a2, a3 in a:
        one = find(a1)
        two = find(a2)
        if one != two:
            b[two] = one
            ans += a3
            cnt += 1
        if cnt == v-1:
            break


v, e = map(int, input().split())
a = []
b = list(range(10001))
ans = 0
cnt = 0

for _ in range(e):
    a.append(list(map(int, input().split())))

# print(a)
a.sort(key=lambda x: x[2])
# print(a)
mst()
print(ans)
