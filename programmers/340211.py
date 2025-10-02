def solution(points, routes):
    visited = set()
    checked = set()
    for route in routes:
        t = 0
        for i in range(len(route)-1):
            sr, sc = points[route[i]-1]
            er, ec = points[route[i+1]-1]
            step = 1 if sr < er else -1
            for r in range(sr, er, step):
                if (r,sc,t) in visited:
                    checked.add((r,sc,t))
                else:
                    visited.add((r,sc,t))
                t += 1
            step = 1 if sc < ec else -1
            for c in range(sc, ec, step):
                if (er,c,t) in visited:
                    checked.add((er,c,t))
                else:
                    visited.add((er,c,t))
                t += 1
        if (er,ec,t) in visited:
            checked.add((er,ec,t))
        else:
            visited.add((er,ec,t))
    return len(checked)