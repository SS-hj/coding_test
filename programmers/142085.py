import heapq
def solution(n, k, enemy):
    h = enemy[:k]
    heapq.heapify(h)
    for game in range(k, len(enemy)):
        n -= heapq.heappushpop(h,enemy[game])
        if n < 0:
            return game
    return len(enemy)