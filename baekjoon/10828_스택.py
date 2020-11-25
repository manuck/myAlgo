import sys
sys.stdin = open('10828_input.txt')

'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

# 백준에서 input() 대신 sys.stdin.readline()을 사용해야 시간초과가 안뜸

t = int(input())

for case in range(t):
    n = int(input())
    stack = []
    for _ in range(n):
        a = list(map(str, input().split()))
        # print(a, stack)
        if len(a) == 2:
            stack.append(a[1])
        else:
            if a[0] == 'pop':
                if len(stack) > 0:
                    print(stack.pop())
                else:
                    print(-1)
            elif a[0] == 'size':
                print(len(stack))
            elif a[0] == 'empty':
                if len(stack) == 0:
                    print(1)
                else:
                    print(0)
            elif a[0] == 'top':
                if len(stack) > 0:
                    print(stack[-1])
                else:
                    print(-1)
    print()