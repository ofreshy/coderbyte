"""
Using the Python language,
have the function CaesarCipher(str,num) take the str parameter and perform a Caesar Cipher shift on it using the num parameter as the shifting number.
A Caesar Cipher works by shifting each letter in the string N places down in the alphabet
(in this case N will be num). Punctuation, spaces, and capitalization should remain intact.
 For example if the string is "Caesar Cipher" and num is 2 the output should be "Ecguct Ekrjgt".
"""
def CaesarCipher(str,num):
  range_lower = (ord('a'), ord('z'))
  range_upper = (ord('A'), ord('Z'))
  cipher = ''
  for s in str:
      ord_s = ord(s)
      if range_lower[0] <= ord_s <= range_lower[1]:
          ord_s += num
          if ord_s > range_lower[1]:
              ord_s = range_lower[0] + (ord_s - range_lower[1] - 1)
      if range_upper[0] <= ord_s <= range_upper[1]:
          ord_s += num
          if ord_s > range_upper[1]:
              ord_s = range_upper[0] + (ord_s - range_upper[1] - 1)
      cipher += chr(ord_s)
  return cipher



print CaesarCipher('z', 1)