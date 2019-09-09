import sys
sys.stdin = open("1259.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    bars = [[0, 0] for _ in range(N)]
    ans = [[0, 0] for _ in range(N)]
    for i in range(N):
        bars[i][0] = arr[i * 2]
        bars[i][1] = arr[i * 2 + 1]

    # 첫 번째 막대를 찾는다.
    first = 0
    for i in range(N):
        j = 0
        while j < N:
            if i != j and bars[j][1] == bars[i][0]:
                break
            j += 1
        if j == N:
            ans[0][0], ans[0][1] = bars[i][0], bars[i][1]
            break
    # 암나사 = 숫나사 같은 막대를 찾아서 연결
    for i in range(1, N):
        for j in range(N):
            if ans[i - 1][1] == bars[j][0]:
                ans[i][0], ans[i][1] = bars[j][0], bars[j][1]

    print("#%d" % test_case, end="")
    for i in range(len(ans)):
        print(" %d %d" % (ans[i][0], ans[i][1]), end="")
    print()


