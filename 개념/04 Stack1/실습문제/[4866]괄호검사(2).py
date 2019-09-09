import sys
sys.stdin = open("input.txt", "r")


T = int(input())
first = {'(': ')', '{': '}'}
second = {')': '(', '}': '{'}

for test_case in range(1, T + 1):
    instr = input()

    stack = []
    ans = True
    for ch in instr:
        if ch in first:
            stack.append(ch)
        elif ch in second:
            if len(stack) == 0:
                ans = False
                break

            tmp = stack.pop()

            if second[ch] != tmp:
                ans = False
                break

    if ans and len(stack) != 0:
        ans = False

    print("#%d %d" % (test_case, ans))
