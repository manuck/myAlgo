# 1 = 빨강, 2 = 파랑, 3 = 보라
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0 for i in range(10)] for j in range(10)]
    ans = 0

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for x in range(r1, r2 + 1):
            for y in range(c1, c2 + 1):
                arr[x][y] += color
                if arr[x][y] == 3:
                    ans += 1

    print("#%d %d" % (test_case, ans))


