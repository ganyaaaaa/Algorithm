# 두 정수 입력받기
A, B = map(int, input().split())
# 두 수 비교해 결과 출력
if A < B:
    print('<')
elif A > B:
    print('>')
else :
    print('==')