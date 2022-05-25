from itertools import permutations

n = int(input())
k = int(input())
arr = [input() for i in range(n)]
test = list(permutations(arr,k))
A = []
for t in test:
    A += [''.join(t)]
    
print(len(set(A)))