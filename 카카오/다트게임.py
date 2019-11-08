import sys
sys.stdin = open('다트게임_input.txt')

dartResult = input()
print(dartResult)
number = ''
score = []
for i in dartResult:
    if i.isnumeric():
        number += i
    elif i == 'S':
        score.append(int(number)**1)
        number = ''
    elif i == 'D':
        score.append(int(number)**2)
        number = ''
    elif i == 'T':
        score.append(int(number)**3)
        number = ''
    elif i == '*':
        if len(score) != 3:
            for j in range(len(score)):
                score[j] *= 2
        else:
            for j in range(1, len(score)):
                score[j] *= 2
    elif i == '#':
        score[-1] *= -1

print('최종')
print(score)
print(score[-2])
