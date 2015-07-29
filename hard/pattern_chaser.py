"""
Using the Python language,
have the function PatternChaser(str) take str which will be a string and return the longest pattern within the string.
 A pattern for this challenge will be defined as:
 if at least 2 or more adjacent characters within the string repeat at least twice.
 So for example "aabecaa" contains the pattern aa,
 on the other hand "abbbaac" doesn't contain any pattern.
 Your program should return yes/no pattern/null.
 So if str were "aabejiabkfabed" the output should be yes abe.
 If str were "123224" the output should return no null.
 The string may either contain all characters (a through z only), integers, or both.
 But the parameter will always be a string type.
 The maximum length for the string being passed in will be 20 characters.
 If a string for example is "aa2bbbaacbbb" the pattern is "bbb" and not "aa".
 You must always return the longest pattern possible.

"""


def PatternChaser(pattern):

    def pattern_gen(length):
        prev = ''
        for i in xrange(len(pattern) - length + 1):
            cur = pattern[i:i+length]
            if cur != prev:
                prev = cur
                yield cur

    def repeat_pattern():
        s = set()
        for p in patterns:
            if p not in s:
                s.add(p)
            else:
                return p
        return None

    result = ''
    for j in xrange(2, len(pattern) / 2 + 1):
        patterns = pattern_gen(j)
        repeated = repeat_pattern()
        result = repeated if repeated else result

    if result:
        return 'yes ' + result
    else:
        return 'no null'

assert PatternChaser('1123456789110') == 'yes 11'
assert PatternChaser('da2kr32a2') == 'yes a2'
assert PatternChaser('sskfssbbb9bbb') == 'yes bbb'
assert PatternChaser('') == 'no null'
assert PatternChaser('123224') == 'no null'
assert PatternChaser('abcdef12kkk12')
