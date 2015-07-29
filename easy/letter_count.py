def LetterCountI(sentence):
  def most_common(word):
      dic = {}
      for w in word:
          if w not in dic:
              dic[w] = 0
          dic[w] +=1
      return max(dic.values())

  cur_max = -1
  cur_word = None
  for word in sentence.split():
      repeated = most_common(word.lower())
      if repeated > 1 and repeated > cur_max:
          cur_max = repeated
          cur_word = word

  return cur_word if cur_word else -1


print LetterCountI('Today, is the greatest day ever')
print LetterCountI('No words')


