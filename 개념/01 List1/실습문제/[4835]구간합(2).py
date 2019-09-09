import sys
sys.stdin = open("sum_input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    sum = 0
    for i in range(M):
        sum += arr[i]

    i, j = 0, M
    Min = Max = sum
    while j < N:
        sum += (arr[j] - arr[i])
        Min = min(Min, sum)
        Max = max(Max, sum)
        i, j = i + 1, j + 1

    print("#%d %d" % (test_case, Max - Min))


