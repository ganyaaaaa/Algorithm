# 1부터 30까지의 출석번호를 가진 리스트 생성 (처음에는 모든 학생이 과제를 제출하지 않은 상태)
baskets = [i for i in range(1, 31)]

# 제출한 학생들의 출석번호를 저장할 리스트
arr = []

# 28명의 학생이 과제를 제출하므로 28번 반복
for a in range(28):
    i = int(input())        # 과제를 제출한 학생의 출석번호 입력 받기
    arr.append(i)           # 입력받은 출석번호를 arr 리스트에 추가 (추가로 기록)
    baskets.remove(i)       # 제출한 학생의 출석번호를 baskets 리스트에서 제거

# 남은 두 명의 출석번호를 오름차순으로 정렬
baskets.sort()

# 제출하지 않은 학생들 중 출석번호가 가장 작은 학생 출력
print(baskets[0])

# 제출하지 않은 나머지 한 학생의 출석번호 출력
print(baskets[1])