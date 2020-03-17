import sys
sys.stdin = open('가장 긴 팰린드롬_input.txt')

'''
문제 설명
앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.

예를들면, 문자열 s가 abcdcba이면 7을 return하고 abacde이면 3을 return합니다.

제한사항
문자열 s의 길이 : 2,500 이하의 자연수
문자열 s는 알파벳 소문자로만 구성
'''

t = int(input())
for case in range(t):
    s = input()
    answer = 0
    print(s)
    for i in range(len(s)):
        for j in range(1, len(s)+1-i):
            stand = s[i:i+j]
            reverse = stand[::-1]
            if stand == reverse and j > answer:
                answer = j

    print(answer)