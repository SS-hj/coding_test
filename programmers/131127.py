def solution(want, number, discount):
    cnt = 0
    for i in range(len(discount)-9):
        for product, num in zip(want, number):
            if discount[i:i+10].count(product) < num:
                break
        else:
            cnt += 1
    return cnt