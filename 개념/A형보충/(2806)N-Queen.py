
col = [0] * 10

def Possible(r, c):
    for i in range(r):
        if abs(r - i) == abs(c - col[i]):
            return False

    return True

def nQueen(k, n, visit):

    if k == n:
        global cnt
        cnt += 1

    for i in range(n):
        if visit & (1 << i): continue
        if not Possible(k, i): continue
        col[k] = i
        nQueen(k + 1, n, visit | (1 << i))


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    cnt = 0
    nQueen(0, N, 0)
    print('#{} {}'.format(tc, cnt))


