import sys
sys.stdin = open("sort_input.txt")


def getMax(arr, start):
    Max = start
    for i in range(start + 1, len(arr)):
        if arr[Max] < arr[i]:
            Max = i

    arr[start], arr[Max] = arr[Max], arr[start]
    return arr[start]


def getMin(arr, start):
    Min = start
    for i in range(start + 1, len(arr)):
        if arr[Min] > arr[i]:
            Min = i

    arr[start], arr[Min] = arr[Min], arr[start]
    return arr[start]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    print("#%d" % test_case, end="")

    for i in range(10):
        if i & 1:
            print(" %d" % getMin(arr, i), end="")
        else:
            print(" %d" % getMax(arr, i), end="")
    print()
