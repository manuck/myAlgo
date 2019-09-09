import sys
sys.stdin = open("sum_input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    Min = 1000000
    Max = 0

    for start in range(N - M + 1):
        sum = 0
        for i in range(M):
            sum += arr[start + i]

        Min = min(Min, sum)
        Max = max(Max, sum)

    print("#%d %d" % (test_case, Max - Min))


