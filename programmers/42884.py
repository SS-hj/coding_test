def solution(routes):
    routes.sort(reverse=True)
    installed = [routes[0][0]]
    for start,end in routes:
        if not (start <= installed[-1] and end >= installed[-1]):
            installed.append(start)
    return len(installed)