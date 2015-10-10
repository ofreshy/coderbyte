def ABCheck(str):
    for i in range(len(str)-4):
        if str[i] in 'aA' and str[i+4] in 'bB':
            return 'true'
        elif str[i] in 'bB' and str[i+4] in 'aA':
            return 'true'

    return 'false'


print ABCheck('abccccazzzb')