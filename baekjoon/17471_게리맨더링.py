import sys
sys.stdin = open('17471_input.txt')

n = int(input())
a = list(map(int, input().split()))
b = [list(map(int, input().split())) for _ in range(n)]
print(b)