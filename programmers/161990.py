def solution(wallpaper):
    lux, luy, rdx, rdy = 1e9, 1e9, 0, 0
    for r, row in enumerate(wallpaper):
        for c, v in enumerate(row):
            if v == "#":
                lux = min(lux, r)
                luy = min(luy, c)
                rdx = max(rdx, r)
                rdy = max(rdy, c)
    return [lux, luy, rdx+1, rdy+1]