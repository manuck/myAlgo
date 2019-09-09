import sys
sys.stdin = open("input.txt", "r")


class Stack(object):

    def __init__(self, size):
        self.top = -1
        self.size = size
        self.arr = [""] * size

    def push(self, item):
        self.top += 1
        self.arr[self.top] = item

    def isEmpty(self):
        return self.top == -1

    def pop(self):
        ret = self.arr[self.top]
        self.top -= 1
        return ret


T = int(input())
for test_case in range(1, T + 1):
    instr = input()

    stack = Stack(1000)

    ans = True
    for ch in instr:
        if ch == '(' or ch == '{':
            stack.push(ch)
        elif ch == ')' or ch == '}':
            if stack.isEmpty():
                ans = False
                break

            tmp = stack.pop()

            if ch == ')' and tmp != '(':
                ans = False
                break
            if ch == '}' and tmp != '{':
                ans = False
                break

    if ans and not stack.isEmpty():
        ans = False

    print("#%d %d" % (test_case, ans))
