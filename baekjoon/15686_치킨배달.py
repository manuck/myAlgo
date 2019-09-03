import sys
sys.stdin = open('15686_input.txt')


N, M = map(int, input().split())
g = []
for i in range(N):
    g.append(list(map(int, input().split())))

for i in range(N):
    print(g[i])