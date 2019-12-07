import sys
sys.stdin = open('c_input.txt')

t = int(input())

for case in range(t):
    A = list(map(int, input().split()))

    answer = 1000
    for dice in range(1, 7):
        cnt = 0
        for num in A:
            if 7-num == dice:
                cnt += 2
            elif num != dice:
                cnt += 1

        if answer > cnt:
            answer = cnt

    print(answer)
    # print(dice_cnt)