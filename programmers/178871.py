def solution(players, callings):
    check = dict(zip(players, range(len(players))))
    for name in callings:
        i = check[name]
        check[players[i-1]] += 1
        check[name] -= 1
        players[i], players[i-1] = players[i-1], players[i]
    return players