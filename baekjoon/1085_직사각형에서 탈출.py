import sys
sys.stdin = open('1085_input.txt')

'''
한수는 지금 (x, y)에 있다. 직사각형의 왼쪽 아래 꼭짓점은 (0, 0)에 있고, 오른쪽 위 꼭짓점은 (w, h)에 있다. 
직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.
첫째 줄에 x, y, w, h가 주어진다.
'''

x, y, w, h = map(int, input().split())
min_x = min(abs(0-x), abs(w-x))
min_y = min(abs(0-y), abs(h-y))

print(min(min_x, min_y))

