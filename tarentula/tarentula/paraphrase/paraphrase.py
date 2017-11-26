from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn

def tag(sentence):
 words = word_tokenize(sentence)
 words = pos_tag(words)
 return words

def paraphraseable(tag):
 return tag.startswith('NN') or tag == 'VB' or tag.startswith('JJ')

def pos(tag):
 if tag.startswith('NN'):
  return wn.NOUN
 elif tag.startswith('V'):
  return wn.VERB

def synonyms(word, tag):
    lemma_lists = [ss.lemmas() for ss in wn.synsets(word, pos(tag))]
    lemmas = [lemma.name() for lemma in sum(lemma_lists, [])]
    return set(lemmas)

def synonymIfExists(sentence, kw):
 for (word, t) in tag(sentence):
  if word.upper() not in kw:
    if paraphraseable(t):
      syns = synonyms(word, t)
      if syns:
        if len(syns) > 1:
          yield syns.pop()
          continue
  yield word

def paraphrase(sentence, kw):
 return " ".join([x for x in synonymIfExists(sentence, kw)])
