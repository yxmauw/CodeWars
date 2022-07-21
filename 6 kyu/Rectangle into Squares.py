def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    short, long = sorted([lng, wdth])
    squares = []
    while short > 0:
        squares.append(short)
        new_side = long - short
        short, long = sorted([new_side, short])
    return squares
