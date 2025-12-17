def solution(num_list):
    answer = 0
    sum = 0
    mul = 1
    for i in num_list:
        sum += i
        mul *= i
    if sum*sum > mul:
        answer = 1
    return answer
