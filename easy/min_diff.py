
def CountingMinutesI(str):
  def to_minutes(t):
    h, m = map(int, t[:-2].split(':'))
    if t[-2] == 'p':
      h += 12
    return h * 60 + m
  t1, t2 = map(to_minutes, str.split('-'))
  if t1 < t2:
      return t2 - t1
  else:
      return ( t2 + 24*60) - t1


assert CountingMinutesI('9:00am-10:00am') == 60
assert CountingMinutesI('12:30pm-12:00am') == 690
assert CountingMinutesI('1:23am-1:08am') == 1425
