import sys, time
sys.stdin = open('14888_input.txt')

from itertools import permutations as pm

n = int(input())
Num = list(map(int, input().split()))
operator = list(map(int, input().split()))



op = []
for i in range(4):
    for j in range(operator[i]):
        if i == 0:
            op.append('+')
        elif i == 1:
            op.append('-')
        elif i == 2:
            op.append('*')
        elif i == 3:
            op.append('/')

# print(op)
# print(list(pm(op))[0])
op2 = list(pm(op))
# print(op2)

oplen = len(op2[0])
# print(oplen)
maxres = -99999999999
minres = 999999999999
for i in range(len(op2)):
    num = Num[:]
    for j in range(oplen):
        num1 = num.pop(0)
        num2 = num.pop(0)
        if op2[i][j] == '+':
            num.insert(0, num1 + num2)
        elif op2[i][j] == '-':
            num.insert(0, num1 - num2)
        elif op2[i][j] == '*':
            num.insert(0, num1 * num2)
            # print(num)
        elif op2[i][j] == '/':
            if num2 == 0:
                continue
            else:
                if num1 < 0 or num2 < 0:
                    if num1 < 0 and num2 < 0:
                        z = num1 // num2
                        num.insert(0, z)

                    else:
                        num1 = num1*(-1)
                        z = -(num1 // num2)
                        num.insert(0, z)
                else:
                    z = num1//num2
                    num.insert(0, z)

    if maxres < num[0]:
        # print('--------최대-------')
        # print(op2[i])
        # print('-------------------')
        maxres = num[0]
    if minres > num[0]:
        # print('--------최소-------')
        # print(op2[i])
        # print('-------------------')
        minres = num[0]

print(maxres)
print(minres)

# print(time.time()-start)