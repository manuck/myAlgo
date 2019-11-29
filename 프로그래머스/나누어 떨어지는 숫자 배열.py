import sys
sys.stdin = open('나누어 떨어지는 숫자 배열_input.txt')

arr = list(map(int, input().split()))
divisor = int(input())

answer = []

# print(arr)
for i in arr:
    if i % divisor == 0:
        answer.append(i)

answer.sort()
if len(answer) == 0:
    answer.append(-1)
print(answer)