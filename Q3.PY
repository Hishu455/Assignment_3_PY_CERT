from itertools import permutations

wrd,length = input().split()
length = int(length)
permu = list(permutations(wrd,length))
permu.sort()
for element in permu:
    for i in element:
        print(i,end="")
    print()