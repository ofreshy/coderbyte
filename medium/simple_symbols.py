"""
Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence by either returning the string true or false. The str parameter will be composed of + and = symbols with several letters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. The string will not be empty and will have at least one letter.

Use the Parameter Testing feature in the box below to test your code with different arguments.
"""
def SimpleSymbols(str):

  if str[0].isalpha() or str[len(str)-1].isalpha():
      return 'false'

  for i in xrange(1, len(str)-1):
      if str[i].isalpha():
          if str[i-1] != '+' or str[i+1] != '+':
              return 'false'

  return 'true'


assert SimpleSymbols('+d+=3=+s+') == 'true'
assert SimpleSymbols('f++f+') == 'false'
assert SimpleSymbols('+f+f+f') == 'false'

"""
Input = "+d+=3=+s+"Output = "true"
Input = "f++d+"Output = "false"
"""
