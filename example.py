# Import the spaCy open-source library for NLP and its English language model (spaCy must be installed first).
import spacy 

nlp = spacy.load('en_core_web_sm')

# Store two garden path sentences in a list (N.B., I made these two up by following the pattern that I observed in other examples).
gardenpathSentences = [
    "The man who gardens grows in Heathrow.",
    "When Sarah washes hair gets brittle."
]

# Add the following sentences to the list created above.
gardenpathSentences.append("Mary gave the child a Band-Aid.")
gardenpathSentences.append("That Jill is never here hurts.")
gardenpathSentences.append("The cotton clothing is made of grows in Mississippi.")

# Tokenise the sentences and print the output
tokenised_gardenpath_sentences = []

for sentences in gardenpathSentences:
    doc = nlp(sentences)
    tokens = [token.text for token in doc]
    tokenised_gardenpath_sentences.append(tokens)

for tokens in tokenised_gardenpath_sentences:
    print(tokens)

# Perform "named entity recognition" and print output
ner_gardenpath_sentences = []

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    ner_tokens = [(token.text, token.label_) for token in doc.ents]
    ner_gardenpath_sentences.append(ner_tokens)

for ner_tokens in ner_gardenpath_sentences:
    print(ner_tokens)
    
''' 
spaCy has categorised each sentence as follows:
>"The man who gardens grows in Heathrow." [('Heathrow', 'FAC')]
>"When Sarah washes hair gets brittle." [('Sarah', 'PERSON')]
>"Mary gave the child a Band-Aid." [('Mary', 'PERSON')] - N.B., spaCy does not recognise Band-Aid as a brand.
>"That Jill is never here hurts." [('Jill', 'PERSON')]
>"The cotton clothing is made of grows in Mississippi." [('Mississippi', 'GPE')] '''

# Lookup and print the meaning of 'FAC' and 'GPE'
print("Meaning of 'FAC':", spacy.explain('FAC'))
print("Meaning of 'GPE':", spacy.explain('GPE'))

''' 
The two entities I looked up (because 'PERSON' was self-evident) are:

1. [('Heathrow', 'FAC')]. spaCy's description of FAC is "Buildings, airports, highways, bridges, etc", which makes sense in this context because Heathrow is an airport.

2. [('Mississippi', 'GPE')]. spaCy's description of GPE is "Countries, cities, states", which makes sense in this context because Mississippi is a state in the United States.

'''