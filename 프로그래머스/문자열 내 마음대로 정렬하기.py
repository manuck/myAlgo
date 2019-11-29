import sys
sys.stdin = open('문자열 내 마음대로 정렬하기_input.txt')

strings = list(map(str, input().split()))
n = int(input())
answer = []

print(strings)

strings.sort(key=lambda x: (x[n],x))
answer = strings



print(answer)