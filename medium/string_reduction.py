
def StringReduction(str):
    def reduce(two_letters):
        if two_letters[0] == two_letters[1]:
            return two_letters
        elif two_letters in ('ab', 'ba'):
            return 'c'
        elif two_letters in ('ac', 'ca'):
            return 'b'
        else:
            return 'a'

    if len(str) < 2:
        return str

    i = 1
    reduced = reduce(str[0:2])
    ans = ''
    while i < len(str) - 1:
        if len(reduced) == 2:
            ans += reduced[0]
        i += 1
        reduced = reduce(reduced[-1] + str[i])
    if reduced:
        ans += reduced
    return len(ans)


def StringReduction(the_str):
    change = False
    letters = set(['a', 'b', 'c'])
    duo = [the_str[0]]
    final = ''
    for s in the_str[1:]:
        duo.append(s)
        if duo[0] == duo[1]:
            final += duo[0]
            duo = [duo[1]]
        else:
            change = True
            reduced = list((letters - set(duo)))[0]
            duo = [reduced]
    final += ''.join(duo)
    if change:
        return StringReduction(final)
    return len(final)










# print StringReduction('abcabc')
# print StringReduction('ccb')
# print StringReduction('c')
