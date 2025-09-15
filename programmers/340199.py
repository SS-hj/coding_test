def solution(wallet, bill):
    wa, wb, ba, bb = *wallet, *bill
    answer = 0
    while True:
        if (wa>=ba and wb>=bb) or (wa>=bb and wb>=ba):
            break
        if ba >= bb:
            ba = ba//2
        else:
            bb = bb//2
        answer += 1
    return answer