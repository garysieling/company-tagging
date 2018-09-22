import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Hi, I\'m Gary Sieling and I work for Wingspan Technology. IQVIA is hiring')

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

