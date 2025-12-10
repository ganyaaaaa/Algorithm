def solution(num, n):
    answer = 0
    len1 = num % n
    if len1 == 0:
        answer = 1
    else:
        answer = 0
    return answer