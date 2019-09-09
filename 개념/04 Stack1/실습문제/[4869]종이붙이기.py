import sys
sys.stdin = open("input.txt", "r")


memo = [0] * 31
memo[1] = 1
memo[2] = 3
for i in range(3, 31):
    memo[i] = memo[i - 1] + memo[i - 2] * 2

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) // 10
    print("#%d %d" % (test_case, memo[N]))
