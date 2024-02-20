import pickle

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))

def get_tfidf_vectorizer():
    return tfidf
