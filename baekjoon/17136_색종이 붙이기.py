import sys
sys.stdin = open('17136_input.txt')


def check(x, y, a):
    for i in range(a):
        for j in range(a):
            if 0 <= y+i <= 9 and 0 <= x+j <= 9:
                if g[y+i][x+j] == 0:
                    return 0
            else:
                return 0
    return 1

def remove(x, y, size):
    global cnt
    for i in range(size):
        for j in range(size):
            g[y+i][x+j] = 0
            cnt -= 1

def revive(x, y, size):
    global cnt
    for i in range(size):
        for j in range(size):
            g[y+i][x+j] = 1
            cnt += 1



def dfs(x, y, paper, k):
    global res
    if cnt == 0 and paper[0] > -1 and paper[1] > -1 and paper[2] > -1 and paper[3] > -1 and paper[4] > -1:
        if res > k:
            res = k
    elif paper[0] < 0 or paper[1] < 0 or paper[2] < 0 or paper[3] < 0 or paper[4] < 0:
        pass
    else:
        for i in range(10):
            for j in range(10):
                if g[i][j] == 1:
                    for size in range(5, 0, -1):
                        if check(j, i, size):
                            paper[size-1] -= 1
                            remove(j, i, size)
                            dfs(j+size, i, paper, k+1)
                            revive(j, i, size)
                            paper[size - 1] += 1
                    return



g = []
for i in range(10):
    g.append(list(map(int, input().split())))

cnt = 0
res = 25
for i in range(10):
    for j in range(10):
        if g[i][j] == 1:
            cnt += 1
# print(cnt)
paper = [5, 5, 5, 5, 5]

if cnt == 0:
    print(0)
else:
    dfs(0, 0, paper, 0)
    if res == 25:
        print(-1)
    else:
        print(res)