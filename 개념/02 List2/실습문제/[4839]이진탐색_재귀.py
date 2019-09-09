import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def binary_search(lo, hi, key):
    if lo > hi:
        return 0

    mid = (lo + hi) >> 1
    if mid == key:
        return 1
    elif mid < key:
        return binary_search(mid, hi, key) + 1
    else:
        return binary_search(lo, mid, key) + 1


for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())

    cntA = binary_search(1, P, A)
    cntB = binary_search(1, P, B)

    ans = "0"

    if cntA < cntB:
        ans = "A"
    elif cntA > cntB:
        ans = "B"

    print("#%d %s" % (test_case, ans))


