def KnightJumps(str):
    x, y = int(str[1]), int(str[3])

    def in_range(tup):
        return (1 <= tup[0] <= 8) and (1 <= tup[1] <= 8)

    def moves():
        return [
            (x+2, y+1),
            (x+2, y-1),
            (x+1, y+2),
            (x+1, y-2),
            (x-2, y+1),
            (x-2, y-1),
            (x-1, y+2),
            (x-1, y-2),
            ]

    return len([m for m in moves() if in_range(m)])




assert KnightJumps('(4 5)') == 8
assert KnightJumps('(1 1)') == 2
assert KnightJumps('(2 8)') == 3
print KnightJumps('(8 8)')