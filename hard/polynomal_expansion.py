"""
Using the Python language,
have the function PolynomialExpansion(str) take str which will be a string
representing a polynomial containing only (+/-) integers, a letter, parenthesis, and the symbol "^",
 and return it in expanded form.
 For example: if str is "(2x^2+4)(6x^3+3)", then the output should be "12x^5+24x^3+6x^2+12".
 Both the input and output should contain no spaces.
 The input will only contain one letter, such as "x", "y", "b", etc.
 There will only be four parenthesis in the input and your output should contain no parenthesis.
 The output should be returned with the highest exponential element first down to the lowest.

More generally,
the form of str will be: ([+/-]{num}[{letter}[{^}[+/-]{num}]]...[[+/-]{num}]...)(copy) where
"[]" represents optional features,
 "{}" represents mandatory features,
 "num" represents integers and
 "letter" represents letters such as "x".
"""


class Poly(object):
    def __init__(self, modifier=1, letter=None, power=0):
        self.modifier = modifier
        self.letter = letter
        self.power = power

    def __repr__(self):
        if not self.letter or self.power == 0:
            return "%d" % self.modifier
        elif self.power == 1:
            if self.modifier == 1:
                return "%s" % self.letter
            return "%d%s" % (self.modifier, self.letter)
        elif self.modifier == 1:
            return "%s^%d" % (self.letter, self.power)
        return "%d%s^%d" % (self.modifier, self.letter, self.power)

    @classmethod
    def read_poly(cls, poly_string):
        i = 1
        if poly_string[0] == '-':
            modifier = int(poly_string[1]) * -1
            i += 1
        elif poly_string[0] == '+':
            modifier = int(poly_string[1])
            i += 1
        else:
            modifier = int(poly_string[0])

        letter = None
        power = 0
        if len(poly_string) > i:
            letter = poly_string[i]
            if len(poly_string) > i+1:
                power = int(''.join(poly_string[i+2:]))
            else:
                power = 1


        return cls(modifier, letter, power)


def parse(string):
    def parse_poly(poly_expression):
        poly_expression = poly_expression.replace('^-', '#')
        polies = []
        cur = [poly_expression[0]]
        for s in poly_expression[1:]:
            if s in '+-':
                polies.append(''.join(cur).replace('#', '^-'))
                cur = []
            cur.append(s)
        polies.append(''.join(cur))
        return polies

    expressions = [parse_poly(p) for p in string[1:-1].split(')(')]
    return map(Poly.read_poly, expressions[0]),  map(Poly.read_poly, expressions[1])


def PolynomialExpansion(str_exp):
    e1, e2 = parse(str_exp)
    summed = calculate(e1, e2)
    return '+'.join(["%s" % s for s in summed]).replace('+-', '-')


def calculate(e1, e2):
    def add(polies):
        new_modifier = sum([p.modifier for p in polies])
        return Poly(new_modifier, polies[0].letter, polies[0].power)

    def mult(poly1, poly2):
        new_modifier = poly1.modifier * poly2.modifier
        new_letter = poly1.letter or poly2.letter
        new_power = poly1.power + poly2.power
        return Poly(new_modifier, new_letter, new_power)

    expressions = []
    for e11 in e1:
        for e22 in e2:
            expressions.append(mult(e11, e22))

    expressions = sorted(expressions, key=lambda e: -e.power)
    summed = []
    from itertools import groupby
    for k, g in groupby(expressions, lambda x: x.power):
        summed.append(add(list(g)))

    return summed


assert PolynomialExpansion('(2x^2+4)(6x^3+3)') == '12x^5+24x^3+6x^2+12'
assert PolynomialExpansion('(1x)(2x^-2+1)') == 'x+2x^-1'
assert PolynomialExpansion('(-1x^3)(3x^3+2)') == '-3x^6-2x^3'
assert PolynomialExpansion('(1x^2-4)(2x^-2+1)') == 'x^2-2-8x^-2'
assert PolynomialExpansion('(3x)(-7x^3+3)') == '-21x^4+9x'



