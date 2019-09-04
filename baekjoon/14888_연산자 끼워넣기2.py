import sys, time
sys.stdin = open('14888_input.txt')


def dfs(now, index, oper):
    global n, MaxSol, MinSol
    op1, op2, op3, op4 = oper
    if index == n:
        if now > MaxSol:
            MaxSol = now
        if now < MinSol:
            MinSol = now
        return
    if op1 > 0:
        dfs(now + Num[index], index+1, (op1 - 1, op2, op3, op4))
    if op2 > 0:
        dfs(now - Num[index], index + 1, (op1, op2 - 1, op3, op4))
    if op3 > 0:
        dfs(now * Num[index], index + 1, (op1, op2, op3-1, op4))
    if op4 > 0:
        if now < 0:
            dfs(-1*(-now // Num[index]), index + 1, (op1, op2, op3, op4 - 1))
        else:
            dfs(now // Num[index], index + 1, (op1, op2, op3, op4 - 1))




n = int(input())
Num = list(map(int, input().split()))
operator = list(map(int, input().split()))

# print(n)
# print(Num)
# print(operator)
MaxSol = -9999999999999
MinSol = 9999999999999
dfs(Num[0], 1, operator)
print(MaxSol)
print(MinSol)