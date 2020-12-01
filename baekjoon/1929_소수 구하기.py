import sys
sys.stdin = open('1929_input.txt')

'''
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
'''
import math

m, n = map(int, input().split())

array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True:    # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
# print(array)
for i in range(2, n+1):
    if array[i] and i >= m:
        print(i)