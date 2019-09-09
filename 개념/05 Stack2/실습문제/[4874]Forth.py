import sys
sys.stdin = open("5286.txt", "r")


def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return int(a / b)


T = int(input())
for tc in range(1, T + 1):
    exp = map(str, input().split())

    stack = []
    isOk = True
    for token in exp:
        if token == '.': break
        if token in ['+', '-', '*', '/']:
            if len(stack) < 2:
                isOk = False
                break
            opnd2 = stack.pop()
            opnd1 = stack.pop()
            stack.append(calc(opnd1, opnd2, token))
        else:
            stack.append(int(token))

    print("#%d " % tc, end='')
    if isOk and len(stack) == 1:
        print("%d" % stack[0])
    else:
        print("error")

