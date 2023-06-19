def solution(number, limit, power):
    arr = [1]*(number+1)
    answer = 1
    for i in range(2,number+1):
        for j in range(i,number+1,i):
            arr[j] += 1
        answer += power if arr[i]>limit else arr[i]
    return answer