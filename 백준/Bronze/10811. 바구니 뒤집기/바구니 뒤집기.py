N, M = map(int,input().split())
baskets = []
for i in range(1,N+1):
    baskets.append(i)
# baskets = list(range(1, N + 1))

for j in range(M):
     a, b = map(int, input().split())
     baskets = baskets[:a-1] + list(reversed(baskets[a-1:b])) + baskets[b:]
      
print(*baskets)