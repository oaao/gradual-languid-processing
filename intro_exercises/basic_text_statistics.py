from nltk import FreqDist
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

fd = FreqDist(text1)

def find_long_words(text, min_length, min_freq=1):

    t = set(text)
    f = FreqDist(text)

    return sorted([w for w in t if len(w) >= min_length and f[w] >= min_freq])


if __name__ == '__main__':

    print(fd)
    print(f'Some statistics for {text1.name}:')
    print(f'5 most common tokens: {fd.most_common(5)}')
    print(f'Number of occurrences of "ship": {fd["ship"]}')

    # can we find out anything characteristic about a text by looking at its long words?
    print(f'\nTokens 16 characters or longer in {text1.name}:')
    print(find_long_words(text1, 16))
    print(f'\nTokens 16 characters or longer in {text4.name}:')
    print(find_long_words(text4, 16))
    print(f'\nTokens 16 characters or longer in {text5.name}:')
    print(find_long_words(text5, 16))

    # sort of... what about long-ish words that occur at a reasonable frequency?
    print(f'\nTokens 10 characters or longer, with 15 or more occurrences, in {text1.name}:')
    print(find_long_words(text1, 10, min_freq=15))
    print(f'\nTokens 10 characters or longer, with 15 or more occurrences, in {text4.name}:')
    print(find_long_words(text4, 10, min_freq=15))
    print(f'\nTokens 10 characters or longer, with 15 or more occurrences, in {text5.name}:')
    print(find_long_words(text5, 10, min_freq=15))