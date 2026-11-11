
import re
import joblib
import nltk
import streamlit as st
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    text = re.sub(r"\$[^$]*\$", " ", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    tokens = [lemmatizer.lemmatize(t) for t in text.split()
              if t not in stop_words and len(t) > 2]
    return " ".join(tokens)

@st.cache_resource
def load_model():
    return joblib.load("best_model.joblib")

bundle = load_model()
pipeline, threshold = bundle["pipeline"], bundle["threshold"]

st.title("Researchly Research Abstract Classifier")
st.write("This app classifies research abstracts as either AI-related or classical research.")

abstract = st.text_area("Enter research abstract:", height=250)

if st.button("Classify Abstract"):
    if not abstract.strip():
        st.warning("Please enter an abstract first.")
    else:
        cleaned = clean_text(abstract)
        prob_ai = pipeline.predict_proba([cleaned])[0, 1]
        st.subheader("Prediction")
        if prob_ai >= threshold:
            st.success("The abstract is classified as: artificial intelligence")
        else:
            st.success("The abstract is classified as: classical research")
        st.caption(f"Model confidence for 'artificial intelligence': {prob_ai:.1%}")
