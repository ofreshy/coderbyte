
"""
 Using the Python language,
 have the function LineOrdering(strArr) read the strArr parameter being passed
 which will represent the relations among people standing in a line.
 The structure of the input will be ["A>B","B>C","A<D",etc..].
 The letters stand for different people and the greater than and less than
 signs stand for a person being in front of someone or behind someone.
  A>B means A is in front of B and B<C means that B is behind C in line.
 For example if strArr is: ["J>B","B<S","D>J"],
  these are the following ways you can arrange the people in line: DSJB, SDJB and DJSB.
  Your program will determine the number of ways people can be arranged in line.
  So for this example your program should return the number 3.
 It also may be the case that the relations produce an impossible line ordering, resulting in zero as the answer.
"""

from itertools import chain, permutations


def LineOrdering(arr):
    def rules_apply(p):
        for r in arr:
            expression = "%s %s %s" % (p.index(r[0]),  r[1],  p.index(r[2]))
            if not eval(expression):
                return False
        return True

    letters = "".join(set([l for l in "".join(arr) if l.isalpha()]))
    perms = permutations(letters)
    valid_perms = [p for p in perms if rules_apply(p)]
    return len(valid_perms)


def LineOrdering(arr):
    rules = [(s[0], s[2]) if s[1] == '>' else (s[2], s[0]) for s in arr]
    letters = "".join(set(chain(*rules)))
    perms = permutations(letters)

    def satisfy_rules(p):
        return all((p.index(r[0]) > p.index(r[1]) for r in rules))

    valid_perms = [p for p in perms if satisfy_rules(p)]
    return len(valid_perms)



