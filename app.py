import streamlit as st
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize

text = "I love learning Natural Language Processing!"
words = word_tokenize(text)
st.write("Tokenization Output:", words)
