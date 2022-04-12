natural_num = set(range(1,10001))
generated_num = set()

def d():
    for i in range(1, 10001):
        for j in str(i):
            i += int(j)
        generated_num.add(i)

    return sorted(natural_num - generated_num)

self_num = d()

for i in self_num:
    print(i)
