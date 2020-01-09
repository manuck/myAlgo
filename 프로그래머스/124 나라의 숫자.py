import sys
sys.stdin = open('124 나라의 숫자_input.txt')

t = int(input())

for case in range(t):
    n = int(input())
    answer = ''
    num_list = [4, 1, 2]
    mok = 1
    na = 1
    while mok != 0:
        mok = n // 3
        na = n % 3
        if na == 0:
            mok -= 1
        n = mok
        answer = str(num_list[na]) + answer

    print(answer)
