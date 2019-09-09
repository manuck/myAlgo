import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    nums = input()
    cnt = [0] * 10

    for i in range(N):            # 인덱스 사용하기
        idx = int(nums[i])
        cnt[idx] += 1

    maxIdx = 0
    for i in range(1, 10):
        if cnt[maxIdx] <= cnt[i]:
            maxIdx = i

    print("#%d %d %d" % (test_case, maxIdx, cnt[maxIdx]))
