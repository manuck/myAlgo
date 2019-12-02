import sys
sys.stdin = open('콜라츠 추측_input.txt')

t = int(input())
for case in range(t):
    num = int(input())
    answer = 0

    while True:
        if num == 1:
            break
        if num % 2 == 0:
            num = num//2
            answer += 1
        elif num % 2 == 1:
            num = num*3 + 1
            answer += 1

    if answer > 500:
        answer = -1
    print(answer)

