import sys
sys.stdin = open('14681_input.txt')



t = int(input())
for case in range(t):
    x = int(input())
    y = int(input())
    answer = 0
    if x > 0 and y > 0:
        answer = 1
    elif x > 0 and y < 0:
        answer = 4
    elif x < 0 and y > 0:
        answer = 2
    elif x < 0 and y < 0:
        answer = 3

    print(answer)