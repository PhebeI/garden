import spacy

nlp = spacy.load('en_core_web_sm')
gardenpathSentences = u"The old man the boat.', 'The complex houses married and single soldiers and their families.','The horse raced past the barn fell.', 'to be led down or up the garden path','The frames are particularly modern in this picture exhibition, because they are made of wood and have been stored in a damp cellar."

doc = nlp(gardenpathSentences)
doc.text.split()
[token.orth_ for token in doc]
print([(token, token.orth_, token.orth) for token in doc])
print([token.orth_ for token in doc if not token.is_punct | token.is_space])
print(spacy.explain("picture"))
# What was the entity and its explanation that you looked up?
    # The entity i looked up was picture
# Did the entity make sense in terms of the word associated with it?
    # It didnt make sense to me though.