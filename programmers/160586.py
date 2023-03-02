def solution(keymap, targets):
    d = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", [200]*26))
    for key in keymap:
        for i, k in enumerate(key):
            d[k] = min(d[k], i+1)
    res = []
    for target in targets:
        cnt = 0
        for t in target:
            if d[t] == 200:
                cnt = -1
                break
            else:
                cnt += d[t]
        res.append(cnt)
    return res