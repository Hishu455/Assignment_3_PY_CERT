from itertools import product

A = list(map(int,input().split()))
B = list(map(int,input().split()))
prd = list(product(A,B))
print(prd)
for i in prd:
    print(i,end=' ')