import sys
sys.stdin = open('소수 찾기_input.txt')

'''
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
 - numbers는 길이 1 이상 7 이하인 문자열입니다.
 - numbers는 0~9까지 숫자만으로 이루어져 있습니다.
 - 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
'''
import itertools
t = int(input())
for case in range(t):
    numbers = input()
    answer = 0
    n = len(numbers)
    numbers = list(numbers)
    tmp = []
    while True:
        num_com = list(itertools.permutations(numbers, n))
        # print(num_com)
        for s in num_com:
            my_num = int(''.join(s))
            if my_num not in tmp:
                tmp.append(my_num)
                if my_num > 1:
                    state = True
                    for f in range(2, my_num):
                        if my_num % f == 0:
                            state = False
                            break
                    if state:
                        print(my_num)
                        answer += 1
        n -= 1
        if n == 0:
            break

    print(answer)
