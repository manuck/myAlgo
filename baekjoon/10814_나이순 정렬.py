import sys
sys.stdin = open('10814_input.txt')

'''
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
이때, 회원들을 나이가 증가하는 순으로, 
나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.
'''

n = int(input())
people = []
number = 1
for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    people.append((age, number, name))
    number += 1

print(people)
people.sort(key=lambda x: (x[0], x[1]))
print(people)
for i in range(n):
    print(people[i][0], people[i][2])