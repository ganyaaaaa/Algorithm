import sys
T = int(sys.stdin.readline())

for i in range(1,T+1):
    A, B = map(int,sys.stdin.readline().split())
    print(f"Case #{i}: {A} + {B} = {A+B}")

# 다른 방법
# import sys
# input = sys.stdin.readline
# T = int(input())

# for i in range(1,T+1):
#     A, B = map(int,input().split())
#     print(f"Case #{i}: {A} + {B} = {A+B}")
