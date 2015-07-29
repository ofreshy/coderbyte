def NumberSearch(str):
  sum_digits = sum([int(d) for d in str if d.isdigit()])
  num_letters = len([s for s in str if s.isalpha()])
  return int(round(float(sum_digits) / num_letters))



# print NumberSearch("H3ello9-9")


