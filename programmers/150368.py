from itertools import product
def solution(users, emoticons):
    res = [0,0]
    for discount in product([40,30,20,10], repeat=len(emoticons)):
        temp = [0,0]
        for user_d, user_m in users:
            money = 0
            for e, d in zip(emoticons, discount):
                if d>=user_d:
                    money += e*(1-d/100)
            if money >= user_m:
                temp[0] += 1
            else:
                temp[1] += money
        res = max(res, temp)
    return res