"""

구름 Lv.2 장마 (https://level.goorm.io/exam/194982/%EC%9E%A5%EB%A7%88/quiz/1)

"""

import sys
N, M = map(int,sys.stdin.readline().split())
height = list(map(int,sys.stdin.readline().split()))
# 중복을 허용하지 않는 집합 set 선언
rain = set()
# 입력받은 날짜만큼 루프
for day in range(1, M+1):
	# 장마의 범위
	s, e = map(int,sys.stdin.readline().split())
		
	# 비가 온 집의 높이 1씩 증가
	for i in range(s-1, e):
		height[i] += 1
		rain.add(i)
		
	# 날짜가 3의 배수일 경우
	if day%3 == 0:
		
		# 2일 이내 비가 온 집의 높이 1씩 감소
		for i in rain:
			height[i] -= 1
			
		# 집합 초기화
		rain = set()
		
height = list(map(str,height))
print(" ".join(height))

"""

[풀이 해설]

 M일까지 매일 비가오는 양 만큼 해당 땅의 높이에 추가하면 된다.

 매일 비가오는 집의 시작 지점에서 끝지점 까지 루프를 돌며 땅의 높이에 1씩 추가하고, rain에 비가온 집의 번호를 각각 추가한다.

 여기서 rain은 파이썬 집합 set으로 중복을 허용하지 않기에 비가 온 집의 명단이 만들어진다.

 일수가 3의 배수가 될때, 지금까지 비가 온 집의 명단을 탐색하여 각각 땅의 높이에 -1씩 추가한다.

 장마가 끝나면 땅의 높이를 반환한다.

"""