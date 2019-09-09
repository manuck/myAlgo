def getNext(x, y):
    for i in range(x, 10):
        for j in range(10):
            if arr[i][j] == 0: continue
            return (i, j)
    return (10, 10)

def isPossible(x, y, size):
    if x + size > 10 or y + size > 10: return False
    possible = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] == 0: return False
    return True

def setValue(x, y, size, val):
    for i in range(x, x + size):
        for j in range(y, y + size):
            arr[i][j] = val

def backtrack(k, x, y):
    global ans
    if k >= ans: return True

    r, c = getNext(x, y)    # 색종이 붙일 위치 찾기(좌상단 좌표)

    if r == 10:
        ans = min(ans, k)
        return True

    ret = False
    for i in range(5, 0, -1):
        if paper[i] and isPossible(r, c, i):
            setValue(r, c, i, 0)
            paper[i] -= 1
            ret |= backtrack(k + 1, r, c)
            paper[i] += 1
            setValue(r, c, i, 1)

    return ret
# ------------------------------------------------
paper = [0, 5, 5, 5, 5, 5]
arr = [list(map(int, input().split())) for _ in range(10)]

ans = 101
if backtrack(0, 0, 0):
    print(ans)
else:
    print(-1)

