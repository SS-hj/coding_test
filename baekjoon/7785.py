n = int(input())
temp = set()
for _ in range(n):
    name, check = input().split()
    if check == "enter":
        temp.add(name)
    else:
        temp.remove(name)
for name in sorted(temp, reverse=True):
    print(name)