def TripleDouble(num1, num2):

    def straight(num, repeat):
        repeats = set([str(i) * repeat for i in range(10)])
        return set([r[0] for r in repeats if r in num])



    straight_triples = straight(str(num1), 3)
    straight_doubles = straight(str(num2), 2)
    for s in straight_triples:
      if s in straight_doubles:
        return 1
    return 0


assert TripleDouble(1000, 100) == 1
assert TripleDouble(451999277, 41177722899) == 1
assert TripleDouble(40005, 554433) == 0
