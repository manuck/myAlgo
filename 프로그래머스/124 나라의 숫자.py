import sys
sys.stdin = open('124 나라의 숫자_input.txt')


'''
문제 설명

124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.
124 나라에는 자연수만 존재합니다.
124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.
10진법	124 나라	10진법	124 나라
1	    1	        6	    14
2	    2	        7	    21
3	    4	        8	    22
4	    11	        9       24
5	    12	        10	    41

제한사항
n은 500,000,000이하의 자연수 입니다.

'''


t = int(input())

for case in range(t):
    n = int(input())
    answer = ''
    num_list = [4, 1, 2]
    mok = 1
    na = 1
    while mok != 0:
        mok = n // 3
        na = n % 3
        if na == 0:
            mok -= 1
        n = mok
        answer = str(num_list[na]) + answer

    print(answer)
