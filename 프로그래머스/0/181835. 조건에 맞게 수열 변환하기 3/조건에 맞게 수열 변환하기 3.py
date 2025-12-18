def solution(arr, k):
    answer = []
    
    if k % 2 == 0:
        alp = k
        answer = [new_list + alp for new_list in arr]
    else:
        alp = k
        answer = [new_list * alp for new_list in arr]
    return answer