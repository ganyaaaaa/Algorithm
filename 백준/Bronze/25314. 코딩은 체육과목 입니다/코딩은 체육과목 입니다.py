# N 정의
N = int(input())

# 결과 출력
answer = 'int'
for i in range(N//4):
    answer = 'long ' + answer
print(answer)

# 간단한 버전
# print(int(input())//4 * 'long' + 'int')