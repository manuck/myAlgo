import sys
sys.stdin = open('3975_input.txt')

t = int(input())
index = 0
answer = ['' for i in range(t)]
for case in range(t):
    a, b, c, d = map(int, input().split())
    alice = a / b
    bob = c / d
    if alice > bob:
        answer[index] = 'ALICE'
    elif alice < bob:
        answer[index] = 'BOB'
    else:
        answer[index] = 'DRAW'
    index += 1

for case in range(t):
    print(f'#{case+1} {answer[case]}')