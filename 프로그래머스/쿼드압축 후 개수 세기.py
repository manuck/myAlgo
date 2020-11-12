'''
문제 설명
0과 1로 이루어진 2n x 2n 크기의 2차원 정수 배열 arr이 있습니다.
당신은 이 arr을 쿼드 트리와 같은 방식으로 압축하고자 합니다. 구체적인 방식은 다음과 같습니다.

당신이 압축하고자 하는 특정 영역을 S라고 정의합니다.
만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축시킵니다.
그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역(입출력 예를 참고해주시기 바랍니다.)으로 쪼갠 뒤,
각 정사각형 영역에 대해 같은 방식의 압축을 시도합니다.
arr이 매개변수로 주어집니다. 위와 같은 방식으로 arr을 압축했을 때,
배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

'''
arr = [
[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]],
[[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
]


def solution(arr):
    answer = [0, 0]
    l = len(arr)
    def quad(x, y, n):
        start = arr[y][x]
        for i in range(y, y + n):
            for j in range(x, x + n):
                if arr[i][j] != start:  #  다르면 압축불가
                    next = n // 2
                    quad(x, y, next)
                    quad(x, y + next, next)
                    quad(x + next, y, next)
                    quad(x + next, y + next, next)
                    return
        # 압축가능
        answer[start] += 1
    quad(0, 0, l)
    print(answer)
    return answer


for case in range(2):
    solution(arr[case])