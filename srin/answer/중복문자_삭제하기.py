def solution(characters):
	result = ""
	result += characters[0]
	for i in range(1,len(characters)):
		if characters[i - 1] != characters[i]:
			result += characters[i]
	return result

characters = "senteeeencccccceeee"
ret = solution(characters)

print("solution 함수의 반환 값은", ret, "입니다.")
