import sys
sys.stdin = open('쇠막대기_input.txt')

arrangement = input()
answer = 0
arrangement = arrangement.replace("()", "ㅣ")
# print(arrangement)
stack = []
for c in arrangement:
    # print(stack)
    if c == '(':
        stack.append('(')
        answer += 1
    elif c == ')':
        stack.pop()
    else:
        answer += len(stack)

print(answer)

