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

    # concordance(s) returns all occurrences of a word, with before-after context.
    #     - concordance lookup on a string builds an index to speed future lookups
    print(f'\nCONCORDANCES for "monstrous" in: {text1.name}')
    print(text1.concordance('monstrous'))

    # similar(s) returns words which have similar immediate contexts to those of s
    #     - i.e. if "the {s or x} pictures", "a {s or x} size", then s and x are similar words
    print(f'\nSIMILARITIES for "monstrous" in: {text1.name}')
    print(text1.similar('monstrous'))
    print(f'\nSIMILARITIES for "monstrous" in: {text2.name}')
    print(text2.similar('monstrous'))

    # common_contexts(['a', 'b' ...]) shows only the contexts shared by two+ words
    print(f'\nCOMMON CONTEXTS ["monstrous", "very"] in: {text1.name}')
    print(f'{text1.common_contexts(["monstrous", "very"])}')
    print(f'\nCOMMON CONTEXTS ["monstrous", "very"] in: {text2.name}')
    print(f'{text2.common_contexts(["monstrous", "very"])}')
