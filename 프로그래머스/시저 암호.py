import sys
sys.stdin = open('시저 암호_input.txt')

t = int(input())

for case in range(t):
    s = str(input())
    n = int(input())
    answer = ''

    # print(s)
    for i in s:
        state = True
        if i.isupper():
            state = True
        else:
            state = False

        if i != ' ':
            if state and ord(i) + n > 90:
                answer += chr((ord(i) + n) % 90 + 64)
            elif not state and ord(i) + n > 122:
                answer += chr((ord(i) + n) % 122 + 96)
            else:
                answer += chr((ord(i) + n))
        else:
            answer += ' '
    print(answer)
