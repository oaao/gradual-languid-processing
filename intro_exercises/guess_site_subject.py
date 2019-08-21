import requests

from bs4 import BeautifulSoup

from nltk import FreqDist
from nltk.corpus import stopwords


class SubjectGuesser:

    def __init__(self, url):

        self.url_req           = url
        self.url_resp          = None
        self.html              = None
        self.clean_text_tokens = None

        self._text_html_scrubbed  = None
        self._text_tokenized      = None
        self._text_sifted         = None

        self.get_content(url)

    def _scrub_html(self, html):
        bs            = BeautifulSoup(html, 'html.parser')
        scrubbed_text = bs.get_text(strip=True)

        return scrubbed_text

    def _tokenize(self, text):
        return [t for t in text.split()]

    def _sift_stopwords(self, token_list):

        sw = stopwords.words('english')
        return [t for t in token_list if t not in sw]

    def _tabulate(self, token_dict):

        pairs = sorted(token_dict.items(), key=lambda x: x[1], reverse=True)
        return pairs

    def get_content(self, url):

        response  = requests.get(url)

        self.url_resp = response.url
        self.html     = response.text

        self._text_html_scrubbed = self._scrub_html(self.html)
        self._text_tokenized     = self._tokenize(self._text_html_scrubbed)
        self._text_sifted        = self._sift_stopwords(self._text_tokenized)

        self.clean_text_tokens = self._text_sifted

    def plot(self):

        if self.clean_text_tokens:
            freq = FreqDist(self.clean_text_tokens)

            for k, v in self._tabulate(freq):
                print(f'{v:3} : {k}')

            freq.plot(20, title=self.url_resp, cumulative=False)

        else:
            raise Exception('No cleaned, tokenized text available')


if __name__ == '__main__':

    sg = SubjectGuesser('https://en.wikipedia.org/wiki/Special:Random')
    sg.plot()
