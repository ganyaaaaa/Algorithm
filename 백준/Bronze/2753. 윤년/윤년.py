# 연도 입력하기
Y = int(input())
# 윤년이면 1, 아니면 0 출력하기
if ((Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0):
    print(1)
else :
    print(0)