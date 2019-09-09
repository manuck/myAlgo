import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    instr = input()

    stack = []
    ans = True
    for ch in instr:
        if ch == '(' or ch == '{':
            stack.append(ch)
        elif ch == ')' or ch == '}':
            if len(stack) == 0:
                ans = False
                break

            tmp = stack.pop()

            if ch == ')' and tmp != '(':
                ans = False
                break
            if ch == '}' and tmp != '{':
                ans = False
                break

    if ans and len(stack) != 0:
        ans = False

    print("#%d %d" % (test_case, ans))
