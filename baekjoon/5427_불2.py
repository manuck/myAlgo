import sys
sys.stdin = open('5427_input.txt')


def bfs():
    global mylist

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(len(mylist)):
        visited[mylist[i][1]][mylist[i][0]] = (0, mylist[i][2])

    print(visited)
    while mylist:
        x, y, what = mylist.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <







    return 0

t = int(input())

for case in range(1):
    # print('-------------case---------------------')
    w, h = map(int, input().split())
    g = []
    visited = [[1000000 for _ in range(w)]for _ in range(h)]
    visitedMe = [[1000000 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        g.append(list(str(input())))

    for i in range(h):
        print(g[i])

    mylist = []
    for i in range(h):
        for j in range(w):
            if g[i][j] == '*':
                mylist.append([j, i, 1])
            if g[i][j] == '@':
                meX = j
                meY = i
    mylist.append([meX, meY, 2])

    print(mylist)
    bfs()