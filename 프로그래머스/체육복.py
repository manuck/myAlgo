import sys
sys.stdin = open('체육복_input.txt')

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))
answer = 0
clothes = [1] * n
for i in lost:
    clothes[i-1] -= 1

for i in reserve:
    clothes[i-1] += 1

if clothes[0] == 0 and clothes[1] == 2:
    clothes[0] = 1
    clothes[1] -= 1

for i in range(1, len(clothes)-1):
    if clothes[i] == 0 and clothes[i-1] == 2:
        clothes[i] = 1
        clothes[i-1] -= 1

    elif clothes[i] == 0 and clothes[i+1] == 2:
        clothes[i] = 1
        clothes[i+1] -= 1

for i in clothes:
    if i > 0:
        answer += 1

print(answer)
