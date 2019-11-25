import sys
sys.stdin = open('3499_input.txt')


t = int(input())

for case in range(t):
    n = int(input())
    card = list(map(str, input().split()))
    if n % 2 == 1:
        card_a = card[:(n//2)+1]
        card_b = card[(n//2)+1:]
        print(f'#{case+1}', end=" ")
        for i in range(n // 2):
            print(card_a[i], end=" ")
            print(card_b[i], end=" ")
        print(card_a[~0])
    else:
        card_a = card[:(n // 2)]
        card_b = card[(n // 2):]
        print(f'#{case+1}', end=" ")
        for i in range(n//2):
            print(card_a[i], end=" ")
            print(card_b[i], end=" ")
        print()
