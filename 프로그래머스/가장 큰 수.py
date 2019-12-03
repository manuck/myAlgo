import sys
sys.stdin = open('가장 큰 수_input.txt')

t = int(input())
for case in range(t):
    numbers = list(map(int, input().split()))
    answer = ''
    s = []
    for number in numbers:
        original = number
        while number < 1000:
            number *= 10
        s.append([number, original])
    # print(s)
    s = sorted(s, key=lambda x: (-x[0], x[1]))
    answer = str(int("".join([str(number[1]) for number in s])))
    print(answer)
