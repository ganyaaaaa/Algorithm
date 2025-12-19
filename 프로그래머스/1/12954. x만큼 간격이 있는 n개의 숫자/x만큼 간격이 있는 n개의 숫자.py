def solution(x, n):
    answer = []
    num = x 

    while len(answer) < n:
        answer.append(num)  # 리스트에 현재 숫자 추가
        num = num + x      # 숫자를 x만큼 키움 (다음 숫자로)

    return answer
