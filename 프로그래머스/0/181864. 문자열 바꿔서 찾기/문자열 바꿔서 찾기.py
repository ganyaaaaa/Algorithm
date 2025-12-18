def solution(myString, pat):
    answer = 0
    table = str.maketrans("AB", "BA")
    result = myString.translate(table)

    if pat in result:
        answer = 1
    else:
        answer = 0
    return answer
