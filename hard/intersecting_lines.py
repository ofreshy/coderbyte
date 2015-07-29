"""
Using the Python language,
have the function IntersectingLines(strArr) take strArr which will be an array of 4 coordinates in the form: (x,y).
Your program should take these points where the first 2 form a line and the last 2 form a line, and determine whether the lines intersect,
 and if they do, at what point.
 For example: if strArr is ["(3,0)","(1,4)","(0,-3)","(2,3)"], then the line created by (3,0) and (1,4) and the line created by (0,-3) (2,3) intersect at (9/5,12/5).
  Your output should therefore be the 2 points in fraction form in the following format: (9/5,12/5).
  If there is no denominator for the resulting points, then the output should just be the integers like so: (12,3).
  If any of the resulting points is negative, add the negative sign to the numerator like so: (-491/63,-491/67).
  If there is no intersection, your output should return the string "no intersection".
  The input points and the resulting points can be positive or negative integers.
"""


class Ratio(object):
    def __init__(self, top, bot=1):
        if bot == 0:
            raise ArithmeticError("bot cannot be 0")

        self.top = top if bot > 0 else -top
        self.bot = abs(bot)
        self._zamzem()

    def __add__(self, other):
        return Ratio(other.bot*self.top + self.bot * other.top, self.bot * other.bot)

    def __sub__(self, other):
        return Ratio(other.bot*self.top - self.bot * other.top, self.bot * other.bot)

    def __mul__(self, other):
        return Ratio(self.top * other.top, self.bot * other.bot)

    def __div__(self, other):
        return self * Ratio(other.bot, other.top)

    def __eq__(self, other):
        # Remember that the ratios are always in lowest denom
        if self.top != other.top:
            return False
        return self.top == 0 or self.bot == other.bot

    def _zamzem(self):
        if self.top == 0:
            self.bot = 1
            return

        min_num = min(abs(self.top), abs(self.bot))
        i = min_num
        largest = None
        while not largest:
            if self.top % i == 0 and self.bot % i == 0:
                largest = i
            i -= 1

        self.top /= largest
        self.bot /= largest

    def __repr__(self):
        if self.bot == 1:
            return "%d" % self.top
        return "%d/%d" % (self.top, self.bot)


class Line(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def from_points(cls, p0, p1):
        x0, y0, x1, y1 = map(Ratio, [p0[0], p0[1], p1[0], p1[1]])
        if x1 - x0 == Ratio(0):
            a = None
            b = x1
        else:
            a = (y1 - y0) / (x1 - x0)
            b = y1 - a * x1
        return cls(a, b)

    def intersect(self, other):
        if self.a is None:
            return self.b, other.y(self.b)
        if self.a == other.a:
            if self.b == other.b:
                raise ArithmeticError('All points')
            return None

        x = (other.b - self.b) / (self.a - other.a)
        y = self.y(x)
        return x, y

    def y(self, x):
        if self.a is None:
            return x, x
        return self.a * x + self.b

    def __repr__(self):
        if self.a is None:
            return "y=NAF(%s)" % self.b
        if self.a == Ratio(0):
            return "y=%s" % self.b
        return "y=%sX+%s" % (self.a, self.b)



def IntersectingLines(strArr):
    ps = [map(int, s[1:-1].split(',')) for s in strArr]
    l0 = Line.from_points(ps[0], ps[1])
    l1 = Line.from_points(ps[2], ps[3])

    ans = l0.intersect(l1)
    return '(%s,%s)' % (str(ans[0]), str(ans[1])) if ans else 'no intersection'


assert "%s" % Ratio(2, 3) == "2/3"
assert "%s" % Ratio(9, 3) == "3"
assert "%s" % Ratio(3, 9) == "1/3"
assert "%s" % (Ratio(2, 3) + Ratio(1, 3)) == "1"
assert "%s" % (Ratio(2, 3) + Ratio(2, 3)) == "4/3"
assert "%s" % (Ratio(2, 3) * Ratio(1, 3)) == "2/9"
assert "%s" % (Ratio(6, 3) * Ratio(1, 3)) == "2/3"



assert IntersectingLines(["(0,0)","(0,-1)","(1,1)","(0,1)"]) == "(0,1)"

assert IntersectingLines(["(3,0)", "(1,4)", "(0,-3)", "(2,3)"]) == "(9/5,12/5)"
assert IntersectingLines(["(9,-2)","(-2,9)","(3,4)","(10,11)"]) == "(3,4)"
assert IntersectingLines(["(1,2)","(3,4)","(-5,-6)","(-7,-8)" ]) == "no intersection"
assert IntersectingLines(["(1,-1)","(1,1)","(-5,-5)","(-7,-7)"]) == "(1,1)"
print IntersectingLines(["(100,5)","(6,2)","(2,6)","(5,100)"])








