baskets = []
for a in range(10):
    b = int(input())
    baskets.append(b)
    a = b%42
    baskets.append(a)
    baskets.remove(b)
baskets = set(baskets)
print(len(baskets))