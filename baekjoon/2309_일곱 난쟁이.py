import sys
sys.stdin = open('2309_input.txt')


def comb(n, r, q):
    # 가지치기 조건
    global res
    if r == 0:
        if sum(T) == 100:
            res = T[:7]
            res.sort()
    elif n < r:
        return
    else:
        T[r-1] = people[n-1]
        comb(n-1, r-1, q)
        comb(n-1, r, q)


people = []
for i in range(9):
    people.append(int(input()))

# print(people)
res = []
T = [0] * 9

comb(9, 7, 7)
# print(res)
for i in res:
    print(i)