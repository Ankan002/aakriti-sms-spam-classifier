from utils.get_tfidf_vectorizer import get_tfidf_vectorizer
from utils.get_model import get_model
from utils.transform_text import transform_text
import sklearn

def get_text_spam_prediction(sms: str) -> int:
    tfidf = get_tfidf_vectorizer()
    model = get_model()
    
    transformed_sms = transform_text(sms)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]
    
    return result
