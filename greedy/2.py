n, m, k = map(int,input().split())
b = list(map(int,input().split()))

# m 번 더하고 같은 수를 최대 k번 연속할 수 있을 때, 최대값?

b.sort(reverse=True)

first = b[0]
second = b[1]

# 최대값이 더해지는 개수를 count
# k+1 길이씩 총 m 길이를 반복적으로 rotate할 수 있으므로, m/(k+1)을 해준 뒤, 
# 한 rotate 당 최대값이 k번 연속으로 더해지는 것이니 k를 곱한다.
count = int(m / (k+1))*k
# rotate가 완료되지 못하는 나머지들 만큼 최대값이 또 더해지므로 나머지 값을 count한다.
count += m % (k+1)

res = 0
res += count*first
res += (m-count)*second

print(res)
    
