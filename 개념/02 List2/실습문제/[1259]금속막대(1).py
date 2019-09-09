import sys
sys.stdin = open("1259.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    bars = []
    for i in range(N):
        bars.append((arr[i * 2], arr[i * 2 + 1]))
    ans = [bars[0]]
    bars.pop(0)
    while len(bars) > 0:
        for i in range(len(bars)):
            if bars[i][1] == ans[0][0]:
                ans.insert(0, bars.pop(i))
                break
            elif bars[i][0] == ans[-1][1]:
                ans.append(bars.pop(i))
                break

    print("#{}".format(test_case), end="")
    for a, b in ans:
        print(" %d %d" % (a, b), end="")
    print()


