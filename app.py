import streamlit as st
from textblob import TextBlob

def analyze_sentiment(text):
    text = text.lower().strip()
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

st.title("Student Feedback Sentiment Analysis")

feedback = st.text_area("Enter student feedback")

if st.button("Analyze"):
    st.write("Sentiment:", analyze_sentiment(feedback))
