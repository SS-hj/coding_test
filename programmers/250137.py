from collections import deque
def solution(bandage, health, attacks):
    attacks = deque(attacks)
    last_time = attacks[-1][0]
    max_hp = health
    non_stop_healing = 0
    for t in range(1, last_time+1):
        if attacks[0][0]==t:
            _, p = attacks.popleft()
            non_stop_healing = 0
            health -= p
            if health <= 0:
                return -1
        else:
            health = min(health+bandage[1],max_hp)
            non_stop_healing += 1
            if non_stop_healing == bandage[0]:
                health = min(health+bandage[2],max_hp)
                non_stop_healing = 0
    return health