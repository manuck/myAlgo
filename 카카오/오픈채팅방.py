import sys
sys.stdin = open('오픈채팅방_input.txt')

n = int(input())
record = []
for _ in range(n):
    record.append(input())
answer = []
userDict = dict()
chatLog = []
enterMsg = "%s님이 들어왔습니다."
exitMsg = "%s님이 나갔습니다."
for info in record:
    infoLst = info.split(' ')
    # print("유저 정보", infoLst)
    # print("user Dick", userDict)
    if infoLst[0] == 'Enter':
        userDict[infoLst[1]] = infoLst[2]
        chatLog.append([enterMsg, infoLst[1]])
    elif infoLst[0] == 'Leave':
        chatLog.append([exitMsg, infoLst[1]])
    elif infoLst[0] == 'Change':
        userDict[infoLst[1]] = infoLst[2]
print()
print(chatLog)
print(userDict)
print()
for log in chatLog:
    answer.append(log[0] % userDict[log[1]])


print(answer)
