import sys
sys.stdin = open("5286.txt", "r")


win = {1: 3, 2: 1, 3: 2}


def play(lo, hi):
    if lo == hi:
        return lo

    mid = int((lo + hi)/2)

    l = play(lo, mid)
    r = play(mid + 1, hi)

    if cards[l] == cards[r] or win[cards[l]] == cards[r]:
        return l

    return r


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))

    print("#%d %d" % (test_case, play(0, len(cards) - 1) + 1))




