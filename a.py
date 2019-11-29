import sys
sys.stdin = open('a_input.txt')

s = str(input())
print(s)
answer = True
print(len(s))
if len(s) != 4 and len(s) != 6:
    answer = False

for i in range(len(s)):
    print(s[i].isdigit())
    if not s[i].isdigit():
        answer = False

print(answer)