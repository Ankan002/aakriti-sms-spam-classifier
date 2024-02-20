import nltk
from utils.get_porter_stemmer import get_porter_stemmer
import string
from nltk.corpus import stopwords

def transform_text(text: str) -> str:
    text = text.lower()
    text = nltk.word_tokenize(text)
    ps = get_porter_stemmer()
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)
