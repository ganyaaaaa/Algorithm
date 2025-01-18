# 테스트 케이스 개수 정의
T = int(input())

# 결과 출력하기
for i in range (T):
    A, B = map(int, input().split())  # 각 테스트 케이스에서 A와 B를 입력받음
    print(A+B)