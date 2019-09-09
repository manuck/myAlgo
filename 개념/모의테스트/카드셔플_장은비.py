import sys
import collections
sys.stdin = open('sample_input.txt', 'r')

def dec(x, c):
    L = collections.deque()
    R = collections.deque()
    temp = collections.deque()
    if x >= N // 2:
        for i in range(0, (N // 2)):
            R.append(c[i])
        for i in range((N // 2), N):
            L.append(c[i])
        x = N-x-1
    else:
        for i in range(0, (N // 2)):
            L.append(c[i])
        for i in range((N // 2), N):
            R.append(c[i])

    for i in range((N//2)-x):
        temp.append(L.popleft())
    for i in range(x):
        temp.append(R.popleft())
        temp.append(L.popleft())
    temp.extend(R)
    return temp

def shuffle(card, count):
    global result
    scard = []
    scard.extend(card)

    if count > 5:
        return
    elif result != -1 and result < count:
        return
    for i in range(N):
        if a[i] != scard[i]:
            break
    else:
        if result == -1 or result > count:
            result = count
        return
    for i in range(N):
        if b[i] != scard[i]:
            break
    else:
        if result == -1 or result > count:
            result = count
        return
    for i in range(1, N):
        sscard = dec(i, scard)
        shuffle(sscard, count+1)

T = int(input())
for t in range(T):
    N = int(input())
    first_card = []
    first_card.extend(list(map(int, input().split())))
    a = sorted(first_card)
    b = sorted(first_card, reverse=True)
    result = -1
    shuffle(first_card, 0)
    print('#{} {}'.format(t+1, result))
