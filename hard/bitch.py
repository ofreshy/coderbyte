def gcd(a, b):
    while a % b:
        a, b = b, a % b
    return b

def frac_reduce(num, den):
    g = gcd(num, den)
    return (num/g, den/g)

class Fraction:
    def __init__(self, num, den=1):
        self.num, self.den = frac_reduce(num, den)

    def __neg__(self):
        return Fraction(-self.num, self.den)

    def __add__(self, other):
        if type(other) == type(0):
            return self + Fraction(other)
        elif type(other) != type(self):
            raise TypeError
        return Fraction(self.num * other.den + other.num * self.den, self.den * other.den)

    def __sub__(self, other):
        if type(other) == type(0):
            return self - Fraction(other)
        elif type(other) != type(self):
            raise TypeError
        return self + -other

    def __mul__(self, other):
        if type(other) == type(0):
            return self * Fraction(other)
        elif type(self) != type(other):
            raise TypeError
        return Fraction(self.num * other.num, self.den * other.den)

    def __div__(self, other):
        if type(other) == type(0):
            return self / Fraction(other)
        elif type(other) != type(self):
            raise TypeError
        return Fraction(self.num * other.den, self.den * other.num)

    def __eq__(self, other):
        if other == None:
            return False
        elif type(other) == type(0):
            return self == Fraction(other)
        elif type(other) != type(self):
            raise TypeError
        return self.num == other.num and self.den == other.den

    def __str__(self):
        return str(self.num) if self.den == 1 else '%d/%d' % (self.num, self.den)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        if p1.x == p2.x:
            self.m = None
        else:
            self.m = (p2.y - p1.y) / (p2.x - p1.x)
            self.b = p1.y - self.m * p1.x

    def intersection(self, other):
        if self.m == other.m:
            return None
        elif self.m == None or other.m == None:
            if self.m == None:
                return other.intersection(self)
            return (other.p1.x, self.m * other.p1.x + self.b)

        x = (other.b - self.b) / (self.m - other.m)
        #mm = sorted([self.p1.x, self.p2.x])
        #if x < mm[0] or x > mm[1]:
        #    return None

        return (x, self.m * x + self.b)

def IntersectingLines(strArr):
    points = [Point(a[0], a[1]) for a in [map(Fraction, map(int, s[1:-1].split(','))) for s in strArr]]
    l1 = Line(points[0], points[1])
    l2 = Line(points[2], points[3])

    i = l1.intersection(l2)
    return '(%s,%s)' % (str(i[0]), str(i[1])) if i else 'no intersection'


print (IntersectingLines(["(100,5)","(6,2)","(2,6)","(5,100)"]))
