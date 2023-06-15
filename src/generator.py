import re


class Generator():
    ''' Generates a series of questions from the given paragraph or url or topic.

        Usage:

        ```python
            from src import Generator
            generator = Generator(par=par)
        ```
        Possible arguments:
        - par : paragraph to generate questions from (defaults to None)
        - url : url of the source based on which to generate questions (defaults to None)
        - topic : topic on which to generate questions; the algorithm will search the web and generate questions (defaults to None)
        - type : 'word' or 'sentence', defaults to 'word'
    '''

    def __init__(self, par:str=None, url:str=None, topic:str=None, type='word'):
        self.par = par
        self.url = url
        self.topic = topic
        self.type = type

    def generate(self):
        if not (self.par or self.url or self.topic):
            return("Cannot generate. You must provide one parameter among (par, url, topic).")
        par = self.par
        if self.type == 'word':
            tokens = self.word_tokenize(par)
        elif self.type == 'sentence':
            tokens = self.sentence_tokenize(par)
        else:
            return('Invalid type. Valid types are "word" and "sentence".') 
        return tokens 
    
    def word_tokenize(self, text):
        words = text.strip().split(' ')
        return words
    
    def sentence_tokenize(self, text):
        sentences = re.compile('[.?!] ').split(text)
        return sentences