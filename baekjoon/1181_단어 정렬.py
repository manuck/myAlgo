import sys
sys.stdin = open('1181_input.txt')

'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
'''

n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append((word, len(word)))

print(words)
words = list(set(words))    # 중복제거
print(words)
words.sort(key=lambda x: (x[1], x[0]))  # 정렬
print(words)

for i in range(len(words)):
    print(words[i][0])