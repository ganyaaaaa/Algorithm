def solution(n):
    answer = []
    # 시작하는 숫자 n을 먼저 리스트에 넣기
    answer.append(n)
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        answer.append(n)
    return answer