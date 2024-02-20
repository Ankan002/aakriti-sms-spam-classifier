from nltk.stem.porter import PorterStemmer

ps: PorterStemmer = PorterStemmer()

def get_porter_stemmer() -> PorterStemmer:
    return ps
