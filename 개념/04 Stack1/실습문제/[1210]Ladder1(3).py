import sys
sys.stdin = open('1210.txt')

def DFS(x, y):
    if x == 0: return y

    arr[x][y] = 0

    ret = 0
    if y - 1 >= 0 and arr[x][y - 1]:
        ret = DFS(x, y - 1)
    elif y + 1 < 100 and arr[x][y + 1]:
        ret = DFS(x, y + 1)
    else:
        ret = DFS(x - 1, y)

    return ret

for test_case in range(1, 11):
    N = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    x = y = 0
    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break

    ans = DFS(x, y)
    print("#%d %d" % (test_case, ans))