import sys
sys.stdin = open('a_input.txt')

input = sys.stdin.readline
def find(num):
    if p[num] != num:
        p[num] = find(p[num])
    return p[num]


def union(a, b):
    A = find(a)
    B = find(b)
    if A != B:
        p[B] = A


n, m = map(int, input().split())
p = [i for i in range(n + 1)]

for _ in range(m):
    state, a, b = map(int, input().split())

    if state:
        if find(a) == find(b):
            print("YES")

        else:
            print("NO")

    else:
        union(a, b)

