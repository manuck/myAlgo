import sys
sys.stdin = open('1107_input.txt')


t = int(input())
for case in range(t):
    # page = int(input())
    # m = int(input())
    # answer = 0
    # enable = {str(i) for i in range(10)}
    #
    # if m != 0:
    #     enable -= set(map(str, input().split()))
    # print(enable)
    # min_cnt = abs(100 - page)
    #
    # for num in range(500001):
    #     num = str(num)
    #     for j in range(len(num)):
    #         if num[j] in enable:
    #             break
    #         elif j == len(num) - 1:
    #             min_cnt = min(min_cnt, abs(page - int(num)) + len(str(num)))
    #
    # answer = min_cnt
    # print(answer)

    target = int(input())
    n = int(input())
    if n > 0:
        disable = list(input().split())
    else:
        disable = []
    print(disable)
    mn = 1e9
    print(mn)
    for i in range(1000001):
        for j in disable:
            if j in str(i):
                break
        else:
            mn = min(mn, abs(target - i) + len(str(i)))
    only = abs(target - 100)

    mn = min(only, mn)
    print(mn)