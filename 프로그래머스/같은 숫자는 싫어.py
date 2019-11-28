import sys
sys.stdin = open('같은 숫자는 싫어_input.txt')

arr = list(map(int, input().split()))

answer = []
print(arr)
answer.append(arr[0])
for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
        answer.append(arr[i])

print(answer)
