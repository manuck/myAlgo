import sys
sys.stdin = open('C_Pipes_input.txt')

t = int(input())

for case in range(t):
    n = int(input())
    g = []
    for _ in range(2):
        g.append(list(input()))
    # print(g1)
    # print(g2)
    # print(g)
    x = 0
    y = 0
    state = 'x'
    while True:
        if g[y][x] == '1' or g[y][x] == '2':
            if state == 'x':
                x += 1
            else:
                y = 999
                break
        else:
            if state == 'x':
                if y == 1:
                    y -= 1
                    state = 'y'
                else:
                    y += 1
                    state = 'y'
            else:
                x += 1
                state = 'x'

        if x >= n:
            # print(y)
            break
    if y == 1:
        print('YES')
    else:
        print('NO')

