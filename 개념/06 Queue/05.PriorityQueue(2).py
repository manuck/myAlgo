# 우선순위큐 + 튜플
from heapq import heappush, heappop

Q = []
arr = [(1, 2), (3,2), (2,3), (2, 5), (3, 1), (2, 2), (4, 4), (4, 2), (4, 1), (1, 1)]

for val in arr:
    heappush(Q, val)

while Q:
    print(heappop(Q))
print()