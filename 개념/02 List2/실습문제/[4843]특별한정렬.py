import sys
sys.stdin = open("sort_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = []

    arr.sort()

    print("#%d" % test_case, end="")

    for i in range(5):
        print(" %d" % arr[N - 1 - i], end="")
        print(" %d" % arr[i], end="")

    print()


