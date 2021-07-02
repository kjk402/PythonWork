# 37번 예상 대진표

def solution(n,a,b):
	answer = 0
	while a != b:
		answer += 1
        # 1을 더해서 2로 나누었을 때, 자리수를 맞춰줌
        # 예) 1, 2의 경우는 2, 3으로 해서 나눴을때 몫이 1이 되도록
		a, b = (a+1)//2, (b+1)//2 # 다음 라운드에 진출 했을 때 가지게 될 번호 수
	return answer



print(solution(8,4,7))