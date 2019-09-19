import sys
sys.stdin = open('14889_input.txt')

import itertools

n = int(input())
g = [list(map(int, input().split()))for _ in range(n)]

for i in range(n):
    print(g[i])

a = list(range(n))
b = [0] * n
print(a)
c = list(itertools.combinations(a, n//2))
print(c)
for i in range(len(c)):
    print(c[i])
