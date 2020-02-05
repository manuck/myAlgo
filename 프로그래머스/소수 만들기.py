import sys
sys.stdin = open('소수 만들기_input.txt')

'''
문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 
return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
'''
from itertools import combinations
t = int(input())

for case in range(t):
    nums = list(map(int, input().split()))
    answer = 0
    print(nums)
    a = list(combinations(nums, 3))
    print(a)
    for i in range(len(a)):
        state = True
        for j in range(2, sum(a[i])):
            if sum(a[i]) % j == 0:
                state = False
                break
        if state == True:
            answer += 1

    print(answer)

