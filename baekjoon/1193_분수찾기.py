import sys
sys.stdin = open('1193_input.txt')

'''
이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 
차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.
'''

n = int(input())
answer = ''
cnt = 0
index = 0

for i in range(1, 1000000):
    cnt += i
    if cnt >= n:
        index = i
        break

s = list(range(1, index+1))
if index % 2 == 1:
    answer += str(s[cnt-n]) + '/' + str(s[-(cnt-n+1)])
else:
    answer += str(s[-(cnt - n + 1)]) + '/' + str(s[cnt - n])

print(answer)