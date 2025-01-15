A, B = map(int, input().split())
C = int(input())

# 총 분 계산
total_minutes = B + C

if total_minutes < 60:
    # 총 분이 60 미만인 경우
    B = total_minutes
elif 60 <= total_minutes < 120:
    # 총 분이 60 이상 120 미만인 경우
    A += 1
    B = total_minutes - 60
elif 120 <= total_minutes < 180:
    # 총 분이 120 이상 180 미만인 경우
    A += 2
    B = total_minutes - 120
else:
    # 총 분이 180 이상인 경우
    A += total_minutes // 60
    B = total_minutes % 60

# 24시간제 처리
if A >= 24:
    A %= 24

print(A, B)