import sys
sys.stdin = open('2108_input.txt')

'''
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 
통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.

'''

n = int(input())
a = []
a_dic = {}
answer = []
for _ in range(n):
    k = int(input())
    a.append(k)
    if str(k) in a_dic:
        a_dic[str(k)] += 1
    else:
        a_dic[str(k)] = 1

a.sort()
a_dic = sorted(a_dic.items(), key=(lambda x: x[1]), reverse=True)
# print(a)
# print(a_dic)
answer.append(round(sum(a)/n))
answer.append(a[n//2])
answer_mode = [int(a_dic[0][0])]
if n != 1:
    for i in range(1, len(a_dic)):
        if a_dic[i][1] != a_dic[i-1][1]:
            break
        else:
            answer_mode.append(int(a_dic[i][0]))
    answer_mode.sort()
    if len(answer_mode) != 1:
        answer.append(answer_mode[1])
    else:
        answer.append(answer_mode[0])
else:
    answer.append(answer_mode[0])

answer.append(max(a)-min(a))
for i in range(4):
    print(answer[i])