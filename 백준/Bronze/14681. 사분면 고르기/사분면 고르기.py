# x좌표, y좌표 범위 지정
x = int(input())
y = int(input())

# 사분면 출력
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)