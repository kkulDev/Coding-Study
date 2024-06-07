
"""
프로그래머스 Lv.2 땅따먹기 (https://school.programmers.co.kr/learn/courses/30/lessons/12913)

문제 설명

땅따먹기 게임을 하려고 합니다. 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고,
모든 칸에는 점수가 쓰여 있습니다. 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다.
단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.

예를 들면,
| 1 | 2 | 3 | 5 |
| 5 | 6 | 7 | 8 |
| 4 | 3 | 2 | 1 |

로 땅이 주어졌다면, 1행에서 네번째 칸 (5)를 밟았으면, 2행의 네번째 칸 (8)은 밟을 수 없습니다.
마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를 완성해 주세요.
위 예의 경우, 1행의 네번째 칸 (5), 2행의 세번째 칸 (7), 3행의 첫번째 칸 (4) 땅을 밟아 16점이 최고점이 되므로 16을 return 하면 됩니다.

제한사항

행의 개수 N : 100,000 이하의 자연수
열의 개수는 4개이고, 땅(land)은 2차원 배열로 주어집니다.
점수 : 100 이하의 자연수

"""

def solution(land):
    # 제약이 없는 첫번째 행을 제외한 두번쨰 행 부터 땅따먹기 시작
    for i in range(1, len(land)):
        # 4가지 경우의 수 탐색
        for j in range(4):
            # 이전 행의 땅들 중에서 연속한 열을 제외한 나머지 땅들의 점수 중 가장 큰 점수를 현재 땅의 점수에 합산
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    # 합산이 끝난 4개의 경우의 수 중 가장 큰 값 반환
    return max(land[-1])


"""

문제 해설

                 (j)
    | 1 | 2 | 3 | 5 |
    | 5 | 6 | 7 | 8 |
 (i)| 4 | 3 | 2 | 1 |

land 값이 위와 동일하게 주어지고 i행 j열일 경우 첫번째 행을 밟을 때는 제약이 없지만,

두번쨰 행 부터는 i-1행에서 밟은 열과 같은 열이 아닐경우 규칙에 부합한다.

그리고 최대값을 구해야 하므로 i-1행 나머지 열의 요소중 가장 큰 값을 찾아 i행 j열에 합산해주면 된다.

합산이 다 끝나면 총 합인 마지막 행의 요소 중 가장 큰 값을 반환한다.

"""