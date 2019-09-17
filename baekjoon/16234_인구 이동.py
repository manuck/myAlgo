import sys
sys.stdin = open('16234_input.txt')

N, L, R = map(int, input().split())

g = []
for i in range(N):
    g.append(list(map(int, input().split())))

for i in range(N):
    print(g[i])