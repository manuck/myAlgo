import sys
sys.stdin = open('3009_input.txt')

'''
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
'''

answer_x = 0
answer_y = 0
point_x = {}
point_y = {}
for _ in range(3):
    x, y = map(int, input().split())
    if str(x) in point_x:
        point_x[str(x)] += 1
    else:
        point_x[str(x)] = 1
    if str(y) in point_y:
        point_y[str(y)] += 1
    else:
        point_y[str(y)] = 1

for key, value in point_x.items():
    if value == 1:
        answer_x = int(key)

for key, value in point_y.items():
    if value == 1:
        answer_y = int(key)

print(answer_x, answer_y)