from animations import danger_streamlit_animation
import streamlit as st
from services.get_text_spm_prediction import get_text_spam_prediction

st.title("SMS SPAM CLASSIFIER/CHECKER")
st.text("")
st.text("")
input_sms = st.text_area("Enter the message...or Copy and Paste the message to detect!! ",)
st.text("")
st.write(f'You wrote {len(input_sms)} characters.')
st.text("")
if st.button("Let's Check"):
    result = get_text_spam_prediction(input_sms)
    if result == 1:
        st.warning("OH..NO! IT'S A SPAM !! BEWARE!")
        danger_streamlit_animation.animation()
    else:
        st.success("RELAX!! IT'S NOT A SPAM !")
        st.balloons()

