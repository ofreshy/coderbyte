def NumberEncoding(str):
  letters = {chr(i): i+1-ord('a') for i in range(ord('a'), ord('z')+1)}

  encoded = ''
  for s in str:
      if s.isalpha():
          s = "%d" % (letters[s.lower()])
      encoded += s
  return encoded



print NumberEncoding('jaj-a')