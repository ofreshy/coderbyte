def LookSaySequence(num):
  l = []
  ans = ''
  num_str = str(num)
  for s in num_str:
    if not l or l[-1] == s:
      l.append(s)
    else:
      ans += "%d%s" % (len(l), l[-1])
      l = [s]


  if l:
      ans += "%d%s" % (len(l), l[-1])
  return ans



print LookSaySequence(1211)
print [s for s in str(1234)]