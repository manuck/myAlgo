import sys
sys.stdin = open('1873_input.txt')

def move(a):
    global tankX, tankY, w, h
    if a == 'U':
        if tankY-1 < 0:
            tankY = 0
            g[tankY][tankX] = '^'
        else:
            if g[tankY-1][tankX] == '.':
                tankY -= 1
                g[tankY][tankX] = '^'
                g[tankY+1][tankX] = '.'
            else:
                g[tankY][tankX] = '^'
    elif a == 'D':
        if tankY+1 > h-1:
            tankY = h-1
            g[tankY][tankX] = 'v'
        else:
            if g[tankY+1][tankX] == '.':
                tankY += 1
                g[tankY][tankX] = 'v'
                g[tankY-1][tankX] = '.'
            else:
                g[tankY][tankX] = 'v'
    elif a == 'R':
        if tankX+1 > w-1:
            tankX = w-1
            g[tankY][tankX] = '>'
        else:
            if g[tankY][tankX+1] == '.':
                tankX += 1
                g[tankY][tankX] = '>'
                g[tankY][tankX-1] = '.'
            else:
                g[tankY][tankX] = '>'
    elif a == 'L':
        if tankX-1 < 0:
            tankX = 0
            g[tankY][tankX] = '<'
        else:
            if g[tankY][tankX-1] == '.':
                tankX -= 1
                g[tankY][tankX] = '<'
                g[tankY][tankX+1] = '.'
            else:
                g[tankY][tankX] = '<'
    return 0


def shot():
    global w, h, tankX, tankY
    cannonY = 0
    cannonX = 0
    if g[tankY][tankX] == '^':
        cannonX = tankX
        cannonY = tankY - 1
        while cannonY >= 0:
            if g[cannonY][cannonX] == '#':
                cannonY = -1
            elif g[cannonY][cannonX] == '*':
                g[cannonY][cannonX] = '.'
                cannonY = -1
            else:
                cannonY -= 1


    elif g[tankY][tankX] == 'v':
        cannonX = tankX
        cannonY = tankY + 1
        while cannonY <= (h-1):
            if g[cannonY][cannonX] == '#':
                cannonY = h
            elif g[cannonY][cannonX] == '*':
                g[cannonY][cannonX] = '.'
                cannonY = h
            else:
                cannonY += 1

    elif g[tankY][tankX] == '>':
        cannonX = tankX + 1
        cannonY = tankY
        while cannonX <= (w-1):
            if g[cannonY][cannonX] == '#':
                cannonX = w
            elif g[cannonY][cannonX] == '*':
                g[cannonY][cannonX] = '.'
                cannonX = w
            else:
                cannonX += 1

    elif g[tankY][tankX] == '<':
        cannonX = tankX - 1
        cannonY = tankY
        while cannonX >= 0:
            if g[cannonY][cannonX] == '#':
                cannonX = -1
            elif g[cannonY][cannonX] == '*':
                g[cannonY][cannonX] = '.'
                cannonX = -1
            else:
                cannonX -= 1

    return 0

t = int(input())
# # 0: 아래, 1: 위, 2: 오른쪽, 3: 왼쪽
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

for case in range(t):
    h, w = map(int, input().split())
    g = []
    for i in range(h):
        g.append(list(input()))

    n = int(input())
    command = list(input())
    # print(command)
    tankX = 0
    tankY = 0
    for i in range(h):
        for j in range(w):
            if g[i][j] == '<' or g[i][j] == '^' or g[i][j] == 'v' or g[i][j] == '>':
                tankX = j
                tankY = i

    # print(tankX, tankY)

    for i in command:
        # print(i)
        if i == 'U' or i == 'D' or i == 'R' or i == 'L':
            move(i)
            # print('****************move******************')
            # print(i)
            # for j in range(h):
            #     print(g[j])
        else:
            shot()
            # print('----------------shot-------------------')
            # print(tankX, tankY)
            # for j in range(h):
            #     print(g[j])
    print(f'#{case+1}', end=" ")
    for i in range(h):
        for j in range(w):
            print(g[i][j], end="")

        print()

