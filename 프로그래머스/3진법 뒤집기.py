import sys
sys.stdin = open('3진법 뒤집기_input.txt')

'''
문제 설명
자연수 n이 매개변수로 주어집니다. 
n을 3진법 상에서 앞뒤로 뒤집은 후, 
이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

'''

t = int(input())
for case in range(t):
    n = int(input())
    print()
    print(n)
    answer = 0
    res = ''
    while True:
        n, r = divmod(n, 3)
        # print(n, r)
        res += str(r)
        if n == 0:
            break
    cnt = 0
    for i in range(len(res)-1, -1, -1):
        answer += (3**cnt)*int(res[i])
        cnt += 1

    print(answer)