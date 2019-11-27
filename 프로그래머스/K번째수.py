import sys
sys.stdin = open('K번째수_input.txt')

import copy

array = list(map(int, input().split()))
commands = []
answer = []
for i in range(3):
    commands.append(list(map(int, input().split())))

for i in range(len(commands)):
    array_copy = copy.deepcopy(array[(commands[i][0]-1):commands[i][1]])
    array_copy.sort()
    answer.append(array_copy[commands[i][2]-1])

print(answer)