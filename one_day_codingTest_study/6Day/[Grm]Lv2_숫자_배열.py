"""

구름 Lv.2 숫자 배열 (https://level.goorm.io/exam/175232/%EC%88%AB%EC%9E%90-%EB%B0%B0%EC%97%B4/quiz/1)

"""

import sys
N = int(sys.stdin.readline())
# i : 0 ~ N-1
for i in range(N):
	# j (i*N + j) : 1 ~ N*N 
	print(" ".join([str(i*N+j) for j in range(1, N+1)]))
	
"""

[풀이 해설]

입력받은 N을 N*N 크기의 배열에 1부터 N*N까지 1씩 증가시키면서 값을 넣어주면 쉽게 풀이가 가능하다.

"""