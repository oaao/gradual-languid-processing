from nltk.book import *
"""
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
"""

if __name__ == '__main__':

    # len(t) returns the token length of a given text (words, punctuation/symbols)
    print(f'\n{len(text1)} tokens in: {text1.name}')

    # set(t) returns all unique words
    print(f'\n{len(set(text1))} unique words in: {text1.name}:')

    # comparing unique tokens with all used tokens yields lexical richness:
    lexical_richness = len(set(text1)) / len(text1)
    print(f'\n{lexical_richness:.2%} lexical richness in: {text1.name}')
    print(f'Or, every word in this text is used on average {1 / lexical_richness} times.')

    # count(w) returns the count, and can be used to determine w's percentage of t text:
    ship_count = text1.count('ship')
    print(f'\n{ship_count} occurrences of "ship" in {text1.name}')
    print(f'"ship" takes up {ship_count / len(text1):.2%} of {text1.name}')