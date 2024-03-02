
# app which will summarize our text

# import required modules


import streamlit as st
from summarizer import Summarizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('Agg')

def home():
    st.write('Welcome to Text Summarization')
    st.write('This app will summarize your text')

    raw_text = st.text_area('Enter your text here') 
    if st.button('Summarize'):
        with st.expander('Original Text'):
            st.write(raw_text)
        c1, c2 = st.columns(2)
        with c1:
            with st.expander('Summarized Text'):
                summarizer = Summarizer()
                summarizer = summarizer(raw_text, min_length=50, max_length=150)
                st.write(summarizer)
        with c2:
            with st.expander('Summarized Text'):
                pass
def about():
    st.write('This is a simple example of how to summarize text using Streamlit')
    

# main function

def main():
    st.title('Text Summarization')
    menu = ['Home', 'About']
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == 'Home':
        home()
    else:
        about() 


if __name__ == '__main__':
    main()