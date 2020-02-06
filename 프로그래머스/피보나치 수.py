import sys
sys.stdin = open('피보나치 수_input.txt')

'''
문제 설명
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어

F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, 
solution을 완성해 주세요.

제한 사항
* n은 1이상, 100000이하인 자연수입니다.
'''

t = int(input())

for case in range(t):
    n = int(input())
    answer = 0
    print(n)
    a = [0, 1]
    for i in range(1, n):
        a.append(a[i] + a[i-1])
    print(a)
    answer = a[n] % 1234567
    print(answer)