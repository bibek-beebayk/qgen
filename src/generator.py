
class Generator():

    def __init__(self, par=None, url=None, topic=None, type='word'):
        self.par = par
        self.url = url
        self.topic = topic
        self.type = type

    def generate(self):
        par = self.par
        if self.type == 'word':
            tokens = self.word_tokenize(par)
        elif self.type == 'sentence':
            tokens = self.sentence_tokenize(par)
        else:
            print('Invalid type. Valid types are "word" and "sentence".')
        return tokens 
    
    def word_tokenize(self, text):
        tokens = text.strip().split(' ')
        return tokens
    
    def sentence_tokenize(self, text):
        tokens = text.strip().split('.')
        return tokens