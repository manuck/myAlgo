import sys
sys.stdin = open("input.txt", "r")

ans = N = K = 0


def subset(k, n, hap, cnt):
    global ans, N, K            # 전역변수
    if hap == K and cnt == N:
        ans += 1
        return
    if hap > K or cnt > N:
        return
    if k == n:
        return

    subset(k + 1, n, hap, cnt)
    subset(k + 1, n, hap + k, cnt + 1)


T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    ans = 0
    subset(1, 13, 0, 0)

    print("#%d %d" % (test_case, ans))

