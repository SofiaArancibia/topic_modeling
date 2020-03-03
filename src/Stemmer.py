import nltk
from collections import defaultdict
from nltk import SnowballStemmer
nltk.download('stopwords')
from nltk.corpus import stopwords
class Stemmer(): # naive class
    def __init__(self):
        self.stems = list()
        self.stemmed_freqs = defaultdict(list)
        self.tokens = list()

    def tokenize(self, document):
        '''
        tokenize document and remove (some of) non-spanish words
        '''
        if not isinstance(document, list):
            if isinstance(document, str):
                self.tokens = document.split(' ')
            else:
                raise TypeError('str or dict expected, {} found.'.format(type(document)))
        else:
            self.tokens = document
    
    def stemm(self, document):
        '''
        document stemming
        '''
        if len(self.tokens) == 0: #empty list
            self.tokenize(document)
        else:
            spanishstemmer = SnowballStemmer('spanish')
            self.stems = [spanishstemmer.stem(token) for token in self.tokens] 
