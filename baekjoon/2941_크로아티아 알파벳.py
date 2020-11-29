import sys
sys.stdin = open('2941_input.txt')

t = int(input())

for case in range(t):
    alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    s = input()
    answer = 0
    print(s)
    for i in alpha:
        s = s.replace(i, ':')
    answer = len(s)
    print(s)
    print(answer)
    print()