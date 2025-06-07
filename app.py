import streamlit as st
import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

text = "I love learning Natural Language Processing!"
words = word_tokenize(text)
st.write("Tokenization Output:", words)
