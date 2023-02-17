from random import randint


def randbool(r, mxr):
    t = randint(0, mxr)
    return t <= r

def randcell(w, h):
    tw = randint(0, w - 1)
    th = randint(0, h - 1)
    return (th, tw)

def randcell2(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    r = randint(0, 3)
    dx = moves[r][0]
    dy = moves[r][1]
    return (x + dx, y + dy)

