# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
strng,no = input().split()
strng = list(strng)
no = int(no)
strng.sort()
for i in range(1,no+1):
    for wrd in combinations(strng,i):
        print(''.join(wrd))
