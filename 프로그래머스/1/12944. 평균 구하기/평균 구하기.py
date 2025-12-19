def solution(arr):
    answer = 0
    
    for i in arr:
        answer += i/len(arr)
    return answer