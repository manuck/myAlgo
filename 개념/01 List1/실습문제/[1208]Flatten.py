import sys
sys.stdin = open('flatten_input.txt', 'r')

for test_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))

    Min = Max = 0
    for i in range(dump):
        Min = Max = 0
        for j in range(1, len(arr)):
            if arr[Min] > arr[j]:
                Min = j
            if arr[Max] < arr[j]:
                Max = j

        arr[Min] += 1
        arr[Max] -= 1

    for j in range(1, len(arr)):
        if arr[Min] > arr[j]:
            Min = j
        if arr[Max] < arr[j]:
            Max = j

    print("#%d %d" % (test_case, max(arr) - min(arr)))

