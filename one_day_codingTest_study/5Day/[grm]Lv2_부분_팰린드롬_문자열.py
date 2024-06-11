"""

구름 Lv.2 부분 팰린드롬 문자열 (https://level.goorm.io/exam/47880/%EB%B6%80%EB%B6%84-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-%EB%AC%B8%EC%9E%90%EC%97%B4/quiz/1)

"""

import sys
# 첫 줄 입력값을 string에 문자열로 저장
string = sys.stdin.readline()
# 부분 팰린드롬 문자열 길이 default
leng = 1
# 부분 문자열의 길이 순환
for i in range(2, len(string)+1):
	# 부분 팰린드롬 문자열 탐색
	for j in range(0,len(string)+1-i):
		word = string[j:j+i]
		# 조건에 부합한 경우 부분 문자열의 길이 갱신
		if word == word[::-1]:
			leng = i
			break
# 조건에 맞는 부분 문자열의 길이 반환
print(leng)