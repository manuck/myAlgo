import sys
sys.stdin = open('완주하지 못한 선수_input.txt')

import collections
participant = list(map(str, input().split()))
completion = list(map(str, input().split()))
answer = ''

'''     효율성 떨어짐
for i in completion:
    participant.remove(i)

answer = participant[0]
'''

person = collections.Counter(participant) - collections.Counter(completion)

answer = list(person.keys())[0]
print(answer)