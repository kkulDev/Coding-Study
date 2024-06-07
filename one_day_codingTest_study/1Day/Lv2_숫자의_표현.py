
"""
프로그래머스 Lv.2 숫자의 표현 (https://school.programmers.co.kr/learn/courses/30/lessons/12924)

문제 설명
Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

제한사항
n은 10,000 이하의 자연수 입니다.

"""

def solution(end):
    front = 1
    case = 1
    # 연속하는 자연수들을 탐색할 범위 설정
    while front < end:
        sum = 0
        # 시작값 front부터 end까지의 범위 탐색
        for num in range(front, end+1):
            if sum < end:
                # 합이 end 이상이 될때까지 연속하는 자연수 합산
                sum += num
            else:
                # 맞을 경우 경우의 수에 포함
                if sum == end:
                    case += 1
                break
        # 탐색할 연속하는 자연수의 시작값 증가
        front += 1
    # 총 경우의 수 반환
    return case

"""

문제 해설


1부터 주어진 값 end까지 범위 중 합이 end인 연속한 수를 탐색하면 된다.

수정 전 코드는 case에 end값 하나인 경우를 미리 추가했어서 end-1까지 탐색했는데,

이럴 경우 1부터 end-1까지(루프 끝까지) 의 합이 end일 경우를 판별하지 못해서

테스트케이스 16번에서 실패가 나왔고, 탐색을 end까지 하는것으로 수정하여 해결하였다.


"""