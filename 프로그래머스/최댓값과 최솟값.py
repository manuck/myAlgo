import sys
sys.stdin = open('최댓값과 최솟값_input.txt')

'''
문제 설명
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 (최소값) (최대값)형태의 문자열을 반환하는 함수, 
solution을 완성하세요.
예를들어 s가 1 2 3 4라면 1 4를 리턴하고, -1 -2 -3 -4라면 -4 -1을 리턴하면 됩니다.

제한 조건
s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.
'''

t = int(input())

for case in range(t):
    s = input()
    answer = ''
    a = list(map(str, s.split()))
    # print(a)
    max = -9999999
    min = 99999999
    for i in a:
        # print(int(i))
        if max < int(i):
            max = int(i)
        if min > int(i):
            min = int(i)

    answer += str(min) + ' ' + str(max)
    print(answer)