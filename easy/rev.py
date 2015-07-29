def DivisionStringified(num1,num2):

  divided = str(int(round(float(num1) / float(num2))))
  buf = ''
  for i, s in enumerate(reversed(divided)):
    buf += s
    if (i+1) % 3 == 0 and (i+1) < len(divided):
      buf += ','

  return ''.join(reversed(buf))




print DivisionStringified(503394930, 43)
