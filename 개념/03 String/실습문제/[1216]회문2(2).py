import sys
sys.stdin = open('1216.txt')

for test_case in range(1, 11):
    N = input()
    arr = []
    for i in range(100):
        arr.append(input())
    ans = 0
    for i in range(100):
        for j in range(100):
            L, R = j, j + 1
            cnt = 0
            while L >= 0 and R < 100:
                if arr[i][L] == arr[i][R]:
                    cnt += 2
                    L, R = L - 1, R + 1
                else:
                    break
            ans = max(ans, cnt)

            L, R = j, j + 1
            cnt = 0
            while L >= 0 and R < 100:
                if arr[L][i] == arr[R][i]:
                    cnt += 2
                    L, R = L - 1, R + 1
                else:
                    break
            ans = max(ans, cnt)

            L, R = j - 1, j + 1
            cnt = 1
            while L >= 0 and R < 100:
                if arr[i][L] == arr[i][R]:
                    cnt += 2
                    L, R = L - 1, R + 1
                else:
                    break
            ans = max(ans, cnt)

            L, R = j - 1, j + 1
            cnt = 1
            while L >= 0 and R < 100:
                if arr[L][i] == arr[R][i]:
                    cnt += 2
                    L, R = L - 1, R + 1
                else:
                    break
            ans = max(ans, cnt)

    print("#%d %s" % (test_case, ans))