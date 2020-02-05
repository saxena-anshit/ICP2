import nltk

text1 = "The dog saw John in the park"
text2 = "The little bear saw the fine fat trout in the rocky brook"

print(text1)
print(text2)

token1 = nltk.word_tokenize(text1)
token2 = nltk.word_tokenize(text2)

print(token1)
print(token2)

# q1 - A) POS TAGGER
pos1 = nltk.pos_tag(token1)
pos2 = nltk.pos_tag(token2)

print(pos1)
print(pos2)

# # q1 - B) NER
# ner1 = nltk.ne_chunk(pos1)
# ner2 = nltk.ne_chunk(pos2)
#
# print(ner1)
# print(ner2)

