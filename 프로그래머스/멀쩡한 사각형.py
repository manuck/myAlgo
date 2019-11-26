import sys
sys.stdin = open('멀쩡한 사각형_input.txt')


w, h = map(int, input().split())

num = 0
if w > h:
    num = w
else:
    num = h

gcd = 0
for i in range(num, 0, -1):
    if w%i == 0 and h%i == 0:
        gcd = i
        break

print((w*h) - gcd*(int(w / gcd) + int(h / gcd) - 1))
