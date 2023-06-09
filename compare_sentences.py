
def compare_sentences(sentence1, sentence2):
  if len(sentence1) != len(sentence2):
    return False
  for word1, word2 in zip(sentence1, sentence2):
    if word1 != word2:
      return False
  return True


def compare(sentence1, sentence2):
  words1=sentence1.split()
  words2=sentence2.split()
  if len(words1) != len(words2):
    return False
  for word1, word2 in zip(words1, words2):
    if word1 != word2:
      return False
  return True