import sys
sys.stdin = open("1259.txt", "r")

def perm(bars, ans, k, n):
    global MAX
    if k > MAX:
        MAX = k
        for i in range(k):
            ans[i][0], ans[i][1] = bars[i][0], bars[i][1]

    if k == n: return

    for i in range(k, n):
        if k != 0 and bars[k - 1][1] != bars[i][0]:
            continue
        bars[i], bars[k] = bars[k], bars[i]
        perm(bars, ans, k + 1, n)
        bars[i], bars[k] = bars[k], bars[i]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    bars = [[0, 0] for _ in range(N)]
    ans = [[0, 0] for _ in range(N)]
    for i in range(N):
        bars[i][0] = arr[i * 2]
        bars[i][1] = arr[i * 2 + 1]
    MAX = 0
    perm(bars, ans, 0, N)

    print("#%d" % test_case, end="")
    for a, b in ans:
        print(" %d %d" % (a, b), end="")
    print()
