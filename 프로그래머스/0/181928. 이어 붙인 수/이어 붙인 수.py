def solution(num_list):
    str_odd = ""  # 홀수만 모을 곳
    str_even = "" # 짝수만 모을 곳

    for num in num_list:
        if num % 2 == 1:
            str_odd += str(num)
        else:
            str_even += str(num)
    answer = int(str_odd) + int(str_even)
    return answer