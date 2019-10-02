import sys
sys.stdin = open('B2_Social Network (hard version)_input.txt')


from collections import deque
n, k = map(int, input().split())
d = deque()
s = set()
for i in map(int, input().split()):
    # print('i', i)
    if i in s:
        continue
    d.appendleft(i)
    s.add(i)
    # print('d', d)
    # print('s', s)
    if len(d) > k:
        s.remove(d.pop())
print(len(d))
print(*d)