import sys
sys.stdin = open('bus_input.txt', 'r') # 파일에서 읽을 때 사용

T = int(input())
for test_case in range (1, T + 1):
    K, N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split())) + [N]

    ans = bus = 0
    for i in range(1, M + 2):
        if arr[i] - arr[i - 1] > K:
            ans = 0
            break
        if arr[i] > bus + K:
            bus = arr[i - 1]
            ans += 1

    print("#%d %d" % (test_case, ans))
