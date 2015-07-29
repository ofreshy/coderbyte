__author__ = 'osharabi'

def DashInsert(str):
    odds = '13579'
    buf = str[0]
    for i in range(1, len(str)):
        if str[i-1] in odds and str[i] in odds:
            buf += '-'
        buf += str[i]
    return buf


assert DashInsert('99946') == '9-9-946'
assert DashInsert('56730') == '567-30'
assert DashInsert('56739') == '567-3-9'


def DashInsertII(num):
    num_str = str(num)
    odds = '13579'
    evens = '2468'
    buf = num_str[0]
    for c in num_str[1:]:
        if c in odds and buf[-1] in odds:
            buf += '-'
        elif c in evens and buf[-1] in evens:
            buf += '*'
        buf += c

    return buf

assert DashInsertII(56647304) == "56*6*47-304"
assert DashInsertII(4546793) == "454*67-9-3"





