import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    instr = input()

    stack = []
    for ch in instr:
        if len(stack) == 0:
            stack.append(ch)
        elif stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    print("#%d %d" % (test_case, len(stack)))
