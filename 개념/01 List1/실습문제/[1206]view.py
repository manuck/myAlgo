import sys
sys.stdin = open("input.txt", "r")

# for test_case in range(1, 11):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     ans = 0
#     for i in range(2, N - 2):
#         Max = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 1])
#
#         if arr[i] > Max:
#                ans += arr[i] - Max
#
#     print("#%d %d" % (test_case, ans))


for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    i = 2
    while i < len(arr) - 2:
        Max = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])

        if arr[i] > Max:
               ans += arr[i] - Max

        i += 1

    print("#%d %d" % (test_case, ans))
