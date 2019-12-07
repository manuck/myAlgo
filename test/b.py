import sys
sys.stdin = open('b_input.txt')

import copy
t = int(input())
for case in range(t):
    S = input()
    S = list(S)
    answer = []
    for i in range(len(S)):
        S_copy = copy.deepcopy(S)
        S_copy.pop(i)
        answer.append(''.join(S_copy))
    print(answer)
    print(min(answer))
    # print(S)