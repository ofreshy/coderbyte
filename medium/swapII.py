def SwapII(str):
  new_str = []
  last_digit = (None, -1)
  for i, s in enumerate(str):
    if s.isalpha():
      s = s.lower() if s.isupper() else s.upper()
    elif s.isdigit():
      if last_digit[0]:
        new_str[last_digit[1]] = s
        s = last_digit[0]
        last_digit = (None, -1)
      elif i+1 < len(str) and str[i+1].isalpha():
        last_digit = s, i
    else:
      last_digit = (None, -1)
    new_str.append(s)
  return ''.join(new_str)




print SwapII("123gg))((")
print SwapII("yolO11")