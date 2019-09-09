import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    ans = 0
    for i in range(1, (1 << 12)):
        sum = cnt = 0
        for j in range(12):
            if (i & (1 << j)) != 0:
                sum += (j + 1)
                cnt += 1
        if cnt == N and sum == K:
            ans += 1

    print("#%d %d" % (test_case, ans))


