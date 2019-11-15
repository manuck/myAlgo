import sys
sys.stdin = open('괄호변환_input.txt')

p = input()
print(p)
def dev_uv(s):
    left_cnt = 0
    right_cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            left_cnt += 1
        else:
            right_cnt += 1
        if left_cnt == right_cnt:
            break
    return s[:i+1], s[i+1:]

def right_string(s):
    state = True
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            state = False
            break
    return state

def solution(p):
    answer = ''
    if p is '':
        return ''

    u, v = dev_uv(p)

    if right_string(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        u_next = u[1:-1]
        for i in range(len(u_next)):
            if u_next[i] == '(':
                answer += ')'
            else:
                answer += '('
        return answer

ans = solution(p)
print(ans)

