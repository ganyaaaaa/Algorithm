# N입력받기
N = int(input())

# N에 해당되는 구구단 출력
for i in range(1,10):
    print("{} * {} = {}".format(N, i, N * i))