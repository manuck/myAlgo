import sys
sys.stdin = open('2468_input.txt')


def safe(x, y):
    global n, visited
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = [(x, y)]
    # cnt = 1
    # for i in range(n):
    #     print(visited[i])
    # print('-------visit---------')
    visited[y][x] = 1
    while q:
        x, y = q.pop(0)
        # print(x, y)
        # for i in range(n):
        #     print(visited[i])
        # print('-------visit---------')
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n:
                continue
            if ny < 0 or ny >= n:
                continue
            if visited[ny][nx] == 0:
                visited[ny][nx] = 1
                # cnt += 1
                q.append((nx, ny))

    return 0



n = int(input())
g = []
for i in range(n):
    g.append(list(map(int, input().split())))

maxHeight = 1
minHeight = 100

for i in range(n):
    # print(g[i])
    if min(g[i]) < minHeight:
        minHeight = min(g[i])

    if max(g[i]) > maxHeight:
        maxHeight = max(g[i])
# print('--------input--------')

# print(maxHeight, minHeight)

result = 1
for i in range(minHeight, maxHeight):
    # print(i, end=" ")
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if i >= g[j][k]:
                visited[j][k] = 1
    section = 0
    for j in range(n):
        for k in range(n):
            if visited[j][k] == 0:
                safe(k, j)
                section += 1
    # print(section)
    if result < section:
        result = section

print(result)

