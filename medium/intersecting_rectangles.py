"""
Using the Python language,
have the function OverlappingRectangles(strArr) read the strArr parameter being passed
which will represent two rectangles on a Cartesian coordinate plane
and will contain 8 coordinates with the first 4 making up rectangle 1 and the last 4 making up rectange 2.
It will be in the following format: ["(0,0),(2,2),(2,0),(0,2),(1,0),(1,2),(6,0),(6,2)"]
Your program should determine the area of the space where the two rectangles overlap,
and then output the number of times this overlapping region can fit into the first rectangle.

For the above example,
the overlapping region makes up a rectangle of area 2,
and the first rectangle (the first 4 coordinates) makes up a rectangle of area 4,
so your program should output 2.
The coordinates will all be integers.
If there's no overlap between the two rectangles return 0.

"""


class Rec(object):
    def __init__(self, points):
        ys = sorted(points, key=lambda x: x[1])
        self.ty, self.by = ys[-1][1], ys[0][1]
        xs = sorted(points, key=lambda x: x[0])
        self.rx, self.lx = xs[-1][0], xs[0][0]

    def area(self):
        return (self.ty - self.by) * (self.rx - self.lx)

    def detached(self, other):
        return self.by >= other.ty or self.ty <= other.by or self.rx <= other.lx or self.lx >= other.rx

    def contain(self, other):
        return self.by <= other.by and self.ty >= other.ty and self.rx >= other.rx and self.lx <= other.lx

    def locked_area(self, other):
        if self.detached(other):
            return 0
        if self.contain(other):
            return other.area()
        if other.contain(self):
            return self.area()

        top_rec, bottom_rec = (self, other) if self.ty > other.ty else (other, self)
        right_rec, left_rec = (self, other) if self.rx > other.rx else (other, self)
        return (bottom_rec.ty - top_rec.by) * (left_rec.rx - right_rec.lx)



def OverlappingRectangles(strArr):
    cleaned = [map(int, s.strip('()').split(',')) for s in strArr[0].split('),')]
    rec1, rec2 = Rec(cleaned[0:4]), Rec(cleaned[4:8])
    locked_area = rec1.locked_area(rec2)
    if locked_area:
        return rec1.area() / locked_area
    return 0



assert OverlappingRectangles(["(0,0),(2,2),(2,0),(0,2),(1,0),(1,2),(6,0),(6,2)"]) == 2
assert OverlappingRectangles(["(0,0),(0,-2),(3,0),(3,-2),(2,-1),(3,-1),(2,3),(3,3)"]) == 6
assert OverlappingRectangles(["(0,0),(5,0),(0,2),(5,2),(2,1),(5,1),(2,-1),(5,-1)"]) == 3
assert OverlappingRectangles(["(0,0),(5,0),(0,2),(5,2),(12,11),(15,11),(12,20),(15,20)"]) == 0
assert OverlappingRectangles(["(0,0),(5,0),(0,2),(5,2),(3,1),(5,1),(3,-1),(5,-1)"]) == 5
print OverlappingRectangles([("(0,0),(5,0),(0,2),(5,2),(2,1),(5,1),(2,-1),(5,-1)") ])




class Rect:
    def __init__(self, points):
        self.minX = min([p[0] for p in points])
        self.maxX = max([p[0] for p in points])
        self.minY = min([p[1] for p in points])
        self.maxY = max([p[1] for p in points])
        self.w = self.maxX - self.minX
        self.h = self.maxY - self.minY

    def __str__(self):
        return '(%d,%d),(%d,%d) [%d,%d]' % (self.minX, self.minY, self.maxX, self.maxY, self.w, self.h)

    def overlap(self, other):
        o = Rect([
                    (max(self.minX, other.minX), max(self.minY, other.minY)),
                    (min(self.maxX, other.maxX), min(self.maxY, other.maxY))
        ])
        if o.h <= 0 or o.w <= 0:
            return None
        return o

def fit(r, R):
    a = int(R.w / r.w)
    b = int(R.h / r.h)
    c = int(R.w / r.h)
    d = int(R.h / r.w)
    e = int((R.w - a * r.w) / r.h)
    f = int((R.h - b * r.h) / r.w)
    g = int((R.w - c * r.h) / r.w)
    h = int((R.h - d * r.w) / r.h)

    return max(
            a * b + c * f + d * e,
            c * d + g * b + h * a
    )

def OverlappingRectangles(strArr):
    coords = map(float, ''.join([c for c in strArr[0] if c not in '()']).split(','))
    a = Rect(zip(coords[0:8:2], coords[1:8:2]))
    b = Rect(zip(coords[8:16:2], coords[9:16:2]))

    o = a.overlap(b)

    return fit(o, a) if o else 0


print OverlappingRectangles([("(0,0),(5,0),(0,2),(5,2),(2,1),(5,1),(2,-1),(5,-1)") ])