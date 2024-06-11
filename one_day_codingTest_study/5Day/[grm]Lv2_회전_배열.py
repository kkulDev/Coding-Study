"""

구름 Lv.2 회전 배열 (https://level.goorm.io/exam/244404/%ED%9A%8C%EC%A0%84-%EB%B0%B0%EC%97%B4/quiz/1)

"""

import sys
# 첫 줄 입력값을 받아 int 타입으로 치환하여 N과 M에 대입
N, M = map(int,sys.stdin.readline().split())
# 첫 줄 입력값을 받아 각 요소를 int 타입으로 치환하여 list로 만들어 arr에 대입
arr = list(map(int,sys.stdin.readline().split()))
shift = 0
# M회 회전
for i in range(M):
	# 총 시프트 횟수 합산
	shift += arr[shift%N]
# 결과값 반환
print(arr[shift%N])