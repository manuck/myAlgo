import sys
sys.stdin = open('a_input.txt')

import itertools
t = int(input())
for case in range(t):
    answer = []
    clock = list(map(int, input().split()))
    over_cnt = 0

    for digit in clock:
        if digit > 5:
            over_cnt += 1

    if over_cnt > 1:
        answer = []

    else:
        clock_perm = list(itertools.permutations(clock, 4))
        for i in range(len(clock_perm)):
            if clock_perm[i][0] > 2:
                continue
            elif clock_perm[i][0] == 2 and clock_perm[i][1] > 3:
                continue
            elif clock_perm[i][2] > 5:
                continue
            else:
                if clock_perm[i] not in answer:
                    answer.append(clock_perm[i])
    print(len(answer))
    print('-------------------')