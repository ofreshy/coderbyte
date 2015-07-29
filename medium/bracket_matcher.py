def BracketMatcher(str):
  round_brackets = 0
  square_brackets = 0
  total_pairs = 0
  for s in str:
      if s == '(':
          round_brackets += 1
          total_pairs += 1
      elif s == ')':
          if round_brackets < 1:
              return 0
          round_brackets -= 1
      elif s == '[':
          square_brackets += 1
          total_pairs += 1
      if s == ']':
          if square_brackets < 1:
              return 0
          square_brackets -= 1

  if square_brackets != 0 or round_brackets != 0:
      return 0
  if total_pairs == 0:
      return 1
  return "1 %d" % total_pairs


  # code goes here
  text = "Code must be properly"
  more = " indented in Python!"
  return text + more