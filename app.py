from streamlit_extras.let_it_rain import rain
import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import sklearn
ps = PorterStemmer()

def example():
    rain(
        emoji="❌",
        font_size=64,
        falling_speed=1.5,
        animation_length="10",
    )

def transform_Text(Text):
    Text = Text.lower()
    Text = nltk.word_tokenize(Text)

    y = []
    for i in Text:
        if i.isalnum():
            y.append(i)

    Text = y[:]
    y.clear()

    for i in Text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    Text = y[:]
    y.clear()

    for i in Text:
        y.append(ps.stem(i))

    return " ".join(y)

# nltk.download('punkt')
# nltk.download('stopwords')
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("SMS SPAM CLASSIFIER/CHECKER")
st.text("")
st.text("")
input_sms = st.text_area("Enter the message...or Copy and Paste the message to detect!! ",)
st.text("")
st.write(f'You wrote {len(input_sms)} characters.')
st.text("")
if st.button("Let's Check"):

    transformed_sms = transform_Text(input_sms)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]
    if result == 1:
     st.warning("OH..NO! IT'S A SPAM !! BEAWARE!")
     example()
    else:
     st.success("RELAX!! IT'S NOT A SPAM !")
     st.balloons()

