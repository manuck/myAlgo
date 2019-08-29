import sys
sys.stdin = open('2589_input.txt')

n, m = map(int, input().split())

g = []
visited = [[0 for _ in range(m)]for _ in range(n)]
for i in range(n):
    g.append(list(input()))

print(g)
print(visited)
