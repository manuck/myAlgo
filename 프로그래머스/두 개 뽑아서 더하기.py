import sys
sys.stdin = open('두 개 뽑아서 더하기_input.txt')

'''
문제 설명
정수 배열 numbers가 주어집니다. 
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 
오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
'''
import itertools

t = int(input())
for case in range(t):
    numbers = list(map(int, input().split()))
    print(numbers)
    answer = []

    a = list(itertools.combinations(numbers, 2))
    print(a)
    for i in range(len(a)):
        if a[i][0] + a[i][1] not in answer:
            answer.append(a[i][0] + a[i][1])
    answer.sort()
    print(answer)