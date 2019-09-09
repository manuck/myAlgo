import sys
sys.stdin = open("input.txt", "r")


def paper(n):
    if n == 0:
        return 0
    if n == 10:
        return 1
    if n == 20:
        return 3

    return paper(n - 10) + paper(n - 20)*2


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    print("#%d %d" % (test_case, paper(N)))
