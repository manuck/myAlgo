import sys
sys.stdin = open('B_Knights_input.txt')

n = int(input())
g = [['W' for _ in range(n)]for _ in range(n)]

# for i in range(n):
#     print(g[i])

for i in range(n):
    for j in range(n):
        if (i+j)%2 == 1:
            g[i][j] = 'B'
        else:
            g[i][j] = 'W'

for i in range(n):
    print(''.join(g[i]))
