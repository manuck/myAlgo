import sys,time
import collections
sys.stdin = open('Shuffle-O-Matic_input.txt')


start = time.time()
def shuffle(a):
    global N
    q = collections.deque([[a, 0]])
    cnt = 0
    res = 0
    # memo = [a]
    state = False
    while q:
        # print(q)
        # print(memo)
        card, ncnt = q.popleft()
        # print('--------------')
        # print(card)
        # print(ncnt)
        # print('---------------')
        if card == Aans or card == Bans:
            res = ncnt
            break
        lcard = card[:int(N / 2)]
        rcard = card[int(N / 2):N + 1]
        # print(lcard)
        # print(rcard)

        if ncnt > 5:
            res = -1
            break
        for i in range(2):
            z1 = []
            z2 = []
            if i == 0:
                for j in range(len(lcard)):
                    z1.append(lcard[j])
                for j in range(len(rcard)):
                    z1.append(rcard[j])
                # print(z1)
                # if z1 not in memo:
                    # memo.append(z1)
                for j in range((N//2)-1):
                    # print('j: ', j)
                    for k in range(j+1):
                        # print('k+j: ', k+j)
                        z1[(N//2)+(2*k)-j-1], z1[(N//2)+(2*k)-j] = z1[(N//2)+(2*k)-j], z1[(N//2)+(2*k)-j-1]
                    # print(z1)
                    z3 = z1[:]
                    # if z3 not in memo:
                    q.append([z3, ncnt + 1])
                        # memo.append(z3)
            else:
                for j in range(len(rcard)):
                    z2.append(rcard[j])
                for j in range(len(lcard)):
                    z2.append(lcard[j])
                # print(z2)
                # if z2 not in memo:
                    # memo.append(z2)
                q.append([z2, ncnt+1])
                for j in range((N//2)-1):
                    # print('j: ', j)
                    for k in range(j+1):
                        # print('k+j: ', k+j)
                        z2[(N//2)+(2*k)-j-1], z2[(N//2)+(2*k)-j] = z2[(N//2)+(2*k)-j], z2[(N//2)+(2*k)-j-1]
                    # print(z2)
                    z4 = z2[:]
                    # q.append([z4, ncnt + 1])
                    # if z4 not in memo:
                    q.append([z4, ncnt + 1])
                        # memo.append(z4)
            # q.append([z, ncnt+1])
            # print(time.time() - start)
    return res


t = int(input())

# start = time.time()
for case in range(t):
    N = int(input())
    card = list(map(int, input().split()))

    # print(card)

    Aans = list(range(1, N+1))      # 오름차순
    Bans = Aans[::-1]               # 내림차순
    # print(Aans)
    # print(Bans)
    print('#', end="")
    print(case+1, end=" ")
    if card == Aans or card == Bans:
        print(0)
    else:
        # print('go')
        sol = shuffle(card)
        print(sol)
print(time.time() - start)
