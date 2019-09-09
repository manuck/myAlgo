import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def binary_search(p, key):
    lo = 1
    hi = p
    cnt = 0
    while lo <= hi:                 # 탐색 구간 체크
        mid = (lo + hi) >> 1        # 중간 위치 계산
        cnt += 1                    # 비교 횟수 카운팅
        if mid == key:
            break
        elif mid < key:
            lo = mid
        else:
            hi = mid
    return cnt


for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())

    cntA = binary_search(P, A)
    cntB = binary_search(P, B)

    ans = "0"
    if cntA < cntB:
        ans = "A"
    elif cntA > cntB:
        ans = "B"

    print("#%d %s" % (test_case, ans))


