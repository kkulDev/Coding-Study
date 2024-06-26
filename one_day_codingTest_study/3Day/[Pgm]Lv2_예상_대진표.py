"""
프로그래머스 Lv.2 예상 대진표 (https://school.programmers.co.kr/learn/courses/30/lessons/12985)

[문제 설명]

△△ 게임대회가 개최되었습니다. 이 대회는 N명이 참가하고, 토너먼트 형식으로 진행됩니다.

N명의 참가자는 각각 1부터 N번을 차례대로 배정받습니다. 그리고, 1번 ↔ 2번, 3번 ↔ 4번, ... , N-1번 ↔ N번의 참가자끼리 게임을 진행합니다.

각 게임에서 이긴 사람은 다음 라운드에 진출할 수 있습니다. 이때, 다음 라운드에 진출할 참가자의 번호는

다시 1번부터 N/2번을 차례대로 배정받습니다. 만약 1번↔2번 끼리 겨루는 게임에서 2번이 승리했다면 다음 라운드에서 1번을 부여받고,

3번↔4번에서 겨루는 게임에서 3번이 승리했다면 다음 라운드에서 2번을 부여받게 됩니다. 게임은 최종 한 명이 남을 때까지 진행됩니다.

이때, 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 궁금해졌습니다.

게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B가 함수 solution의 매개변수로 주어질 때,

처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return 하는 solution 함수를 완성해 주세요.

단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정합니다.


[제한사항]

N : 21 이상 220 이하인 자연수 (2의 지수 승으로 주어지므로 부전승은 발생하지 않습니다.)
A, B : N 이하인 자연수 (단, A ≠ B 입니다.)


"""

def solution(n,a,b):

    # 총 라운드 수  ex) 16명 -> 0b10000(2) -> 7-3 = 4 round
    Round = len(bin(n))-3

    # 이진탐색을 위해 두 참가자의 오름차순 정렬
    pl_1, pl_2 = sorted([a,b])
    
    # 이진탐색을 위한 범위 low, high와 중간값 mid
    mid = n//2
    low = 0
    high = n
    
    # 두 참가자가 대결할 라운드까지 이진탐색
    while True:
        if pl_1 <= mid and pl_2 > mid:
            break
        # 두 참가자의 번호가 중간의 앞쪽이면
        if pl_1 > mid:
            # 범위 최소값을 중간으로
            low = mid
        # 중간의 뒤쪽이면
        elif pl_2 <= mid:
            # 범위 최대값을 중간으로
            high = mid
        # 범위의 중간값 설정
        mid = (low + high) // 2

        Round -= 1
        
    return Round

"""

[풀이 해설]

처음에 해당 문제를 보고 2명씩 짝지어서 그 중 한명만 올라가고 이를 반복하는 트리구조를 생각했다.

그리고 16명으로 시뮬레이션해본 결과 두 참가자의 대결 이후 라운드는 두 참가자가 중심에서 한 쪽으로 모이는것을 확인했다.

이진탐색으로 양쪽을 검사하여 두 참가자가 중심에서 양쪽에 각각 탐색되면 해당 라운드에 만나게 되는것이므로 해당 라운드를 반환한다.

"""