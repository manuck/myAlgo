import sys
sys.stdin = open("4831_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    station = [0] * (N + 1)
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        station[arr[i]] = 1

    ans = pos = 0
    while pos + K < N:
        for i in range(pos + K, pos, -1):
            if station[i] == 1:
                pos = i
                ans = ans + 1
                break
        else:
            ans = 0
            break

    print('#%d %d' % (test_case, ans))
