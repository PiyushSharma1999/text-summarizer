from random import choice
import streamlit as st

# Summary Pkgs
from gensim.summarization import summarize

# Sumy Summary Pkgs
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Function for Sumy Summarization
def sumy_summarizer(docx):
    parser = PlaintextParser.from_string(docx,Tokenizer('english'))
    lex_summarier = LexRankSummarizer()
    summary = lex_summarier(parser.document,3)
    summary_list=[str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

def main():
    """summary and Entity Checker"""

    st.title('Summary and Entity Checker')

    activities =['Summarize','NER checker','NER for URL']
    choice =st.sidebar.selectbox('Select Activity',activities)

    if choice == 'Summarize':
        st.subheader('Summary with NLP')
        raw_text = st.text_area('Enter text here','Type Here')
        summary_choice = st.selectbox('Summary Choice',['Gensim','Sumy Lex Rank'])
        if st.button('Summarize'):
            
            if summary_choice=='Gensim':
                summary_result=summarize(raw_text)

            elif summary_choice=='Sumy Lex Rank':
                summary_result=sumy_summarizer(raw_text)

            st.write(summary_result)



if  __name__=='__main__':
    main()
