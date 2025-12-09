def solution(my_string, overwrite_string, s):
    result_1 = my_string[:s]
    result_2 = overwrite_string
    result_3 = my_string[s+len(overwrite_string):]
    answer = result_1 + result_2 + result_3
    #answer = ''
    return answer