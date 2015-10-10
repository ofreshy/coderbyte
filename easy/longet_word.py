'''
Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string.
If there are two or more words that are the same length, return the first word from the string with that length.
 Ignore punctuation and assume sen will not be empty.
'''

def LongestWord(sen):
    def lk(w):
        return w[0]

    def lw(w):
        return len([l for l in w if l.isalpha() or l.isdigit()])

    wls = sorted([(lw(w), w) for w in sen.split(' ')], key=lk, reverse=True)
    return wls[0][1]

print (LongestWord("fhdlkfh jfui"))
print (LongestWord("509850498504958 5454"))
