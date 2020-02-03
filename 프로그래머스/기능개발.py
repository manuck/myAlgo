import sys
sys.stdin = open('기능개발_input.txt')

'''
문제 설명
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 
각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 
이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 
각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 
예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
'''

import math

progresses = list(map(int, input().split()))
speeds = list(map(int, input().split()))
answer = []

print(progresses)
print(speeds)

a = []
for i in range(len(progresses)):
    n = (100-progresses[i])/speeds[i]
    a.append(math.ceil(n))
print(a)
index = 0
while True:
    for i in range(len(a)):
        a[i] -= a[index]
    cnt = 0
    for i in range(len(a)):
        if a[i] > 0:
            index = i
            break
        else:
            cnt += 1
    answer.append(cnt)
    print(answer)
# while a:
#     print()
#     print(a)
#     k = a.pop(0)
#     m = 1
#     for i in range(len(a)):
#         a[i] -= k
#         if a[i] <= 0:
#             m += 1
#         else:
#             for j in range(m-1):
#                 a.pop(0)
#             break
#     answer.append(m)

print(answer)
