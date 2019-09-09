import sys
sys.stdin = open("minmax_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    Min = 0xffffff
    Max = 0

    for i in range(N):
        Min = arr[i] if arr[i] < Min else Min
        Max = arr[i] if arr[i] > Max else Max

    print('#%d %d' % (test_case, Max - Min))
