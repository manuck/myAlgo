import sys
import collections
sys.stdin = open('5427_input.txt')


def bfs(x, y, z):
    global w, h
    q = collections.deque([])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    if z == 0:
        # print(x, y)
        visited[x][y] = 0
        q.append((y, x, 1))
        cnt = 1
        while q:
            x, y, ncnt = q.popleft()
            # print(x,y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= w:
                    continue
                if ny < 0 or ny >= h:
                    continue

                if g[ny][nx] == '@' or g[ny][nx] == '.':
                    if visited[ny][nx] > ncnt:
                        visited[ny][nx] = ncnt
                        # cnt += 1
                        q.append((nx, ny, ncnt + 1))

    elif z == 1:
        visitedMe[y][x] = 0
        q.append((x, y, 1))
        cnt = 1
        while q:
            x, y, ncnt = q.popleft()
            # print(x, y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= w:
                    continue
                if ny < 0 or ny >= h:
                    continue

                if g[ny][nx] == '@' or g[ny][nx] == '.':
                    if visitedMe[ny][nx] > ncnt:
                        visitedMe[ny][nx] = ncnt
                        # cnt += 1
                        q.append((nx, ny, ncnt+1))

    return 0


t = int(input())

for case in range(t):
    # print('-------------case---------------------')
    w, h = map(int, input().split())
    g = []
    visited = [[1000000 for _ in range(w)]for _ in range(h)]
    visitedMe = [[1000000 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        g.append(list(str(input())))

    # for i in range(h):
    #     print(g[i])

    fire = []
    goal = []
    for i in range(h):
        for j in range(w):
            if g[i][j] == '@':
                myX, myY = j, i
            if g[i][j] == '*':
                fire.append([i, j])

            if g[i][j] == '.' or g[i][j]:
                if i == 0 or i == h-1 or j == 0 or j == w-1:
                    goal.append((j, i))

    # print(myX, myY)
    # if case == 2:
    #     print(fire)
    for i in range(len(fire)):
        bfs(fire[i][0], fire[i][1], 0)

    # for i in range(h):
    #     print(visited[i])

    bfs(myX, myY, 1)
    # print('---------------------')
    # for i in range(h):
    #     print(visitedMe[i])

    # print(goal)
    # print(goalX, goalY)
    lastx = 1000001
    lasty = 1000001
    zxc = 999999999
    if goal:
        for i in range(len(goal)):
            if visitedMe[goal[i][1]][goal[i][0]] < visited[goal[i][1]][goal[i][0]]:
                lastx = goal[i][0]
                lasty = goal[i][1]
                if visitedMe[goal[i][1]][goal[i][0]] < zxc:
                    zxc = visitedMe[goal[i][1]][goal[i][0]]

    # print(lastx, lasty)
    # if case == 2:
    #     print(goal)

    if lastx < 1000001:
        print(zxc+1)
    else:
        print('IMPOSSIBLE')

