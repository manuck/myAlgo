# 라이브러리 활용
import sys
sys.stdin = open('input.txt', 'r')  # 파일에서 입력받는 경우 사용

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    cnt = {}.fromkeys(str1, 0)    # Dictionary 생성

    for ch in str2:                 # str2의 각 글자 확인
        if ch in cnt:
             cnt[ch] += 1         # Dictionary에 있는 경우 개수 증가

    print('#{} {}'.format(tc, max(cnt.values()))) # 최대 개수 출력
