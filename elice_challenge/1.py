from itertools import permutations

n = input()
number = list(n)
check = sorted(int("".join(k)) for k in set(permutations(number)))

for i in range(len(check)):
    if check[i] == int(n):
        break

print(check[i+1])