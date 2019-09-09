import sys
sys.stdin = open("input.txt", "r")


def paper(n, memo):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 3

    if memo[n] != 0:
        return memo[n]

    memo[n] = paper(n - 1, memo) + paper(n - 2, memo)*2
    return memo[n]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    N = int(N/10)
    memo = [0] * (N + 1)

    print("#%d %d" % (test_case, paper(N, memo)))
