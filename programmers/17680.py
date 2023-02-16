from collections import deque

def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    time = 0
    for city in cities:
        s = city.lower()
        if s in cache:
            cache.remove(s)
            time += 1
        else:
            time += 5
        cache.append(s)
    return time