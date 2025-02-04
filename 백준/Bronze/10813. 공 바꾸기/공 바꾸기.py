N, M = map(int,input().split())
baskets = [i for i in range(1, N+1)]

arr = []
for a in range(M):
    i, j = map(int,input().split())
    baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]

print(*baskets)