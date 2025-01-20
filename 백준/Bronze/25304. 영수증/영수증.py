# 총 금액 정의
X = int(input())

# 총 물건 수 정의
N = int(input())

sum = 0

# 가격이 일치하는지 확인
for i in range(N):
    a, b = map(int,input().split()) # a(물건의 가격), b(물건의 수) 정의
    sum += (a*b)
    
if sum == X:
    print('Yes')
else:
    print('No')