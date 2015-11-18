#  Using python, have a function that takes in a sentence
#  being passed and return the largest word in the string. If there are two or more
#  words that are the same length, return the first word from the string with that length.
#  Ignore punctuation and assume sentence will not be empty.
#  Using python, have a function that takes in a sentence
#  being passed and return the largest word in the string. If there are two or more
#  words that are the same length, return the first word from the string with that length.
#  Ignore punctuation and assume sentence will not be empty.
def largestWord(sen):

    x = max(sen.split(),key=len)
    return x
print (largestWord("I am not a humanbeing"))
