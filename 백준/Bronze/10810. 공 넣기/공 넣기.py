N, M = map(int,input().split())
baskets = [0] * N  # 1번 바구니부터 N번 바구니까지 0으로 초기화

arr = []
for a in range(M):
    i, j, k = map(int,input().split())
    
    # i번 바구니부터 j번 바구니까지 k번 공 넣기
    for b in range(i-1, j):
        baskets[b] = k

print(*baskets) # 리스트 앞에 * 를 붙이면 리스트를 언패킹해서 출력할 수 있게 해준다/[]가 없어진다.