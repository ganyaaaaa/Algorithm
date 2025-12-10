def solution(a, b):
    answer = 0
    len1 = str(a)
    len2 = str(b)
    result1 = str(a) + str(b)
    result2 = str(b) + str(a)
    if result1 < result2 :
        answer = int(result2)
    else:
        answer = int(result1)
    return answer
