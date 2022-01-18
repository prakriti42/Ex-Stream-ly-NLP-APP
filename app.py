import streamlit as st 

#Necessary NLP Packaages 
import nltk
from textblob import TextBlob

#Sumy Packages 
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer



def summarizer(text , sentences):
   
    """Summarize the text."""
    nltk.download('punkt')
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

def sentiment(text):
    """Sentiment Analysis of the text."""
    blob = TextBlob(text)
    return blob.sentiment
 
def main():

    st.set_page_config(
     page_title="NLP APP",
     page_icon=":computer:",
     layout="centered",
     initial_sidebar_state="collapsed",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is an *extremely* cool app!"
     }
 )

 
    st.title("Ex-stream-ly NLP Web App") 
    with st.expander("About the application",expanded=False):
     st.write("""
        This is an application that integrates two use case applications of Natural Language Processing (NLP) that are the summarization of long passages into just few sentences and then detection of the sentiment in the text.
     """)
    
    #Getting the text from the user
    task =  st.selectbox("Select An Action You Want To Perform ",("None","Summarize Text","Detect Sentiment"))
        #Text Summarizer 
    if task == "Summarize Text":
        InputText = st.text_area( "Paste the text that you want to summarize here.", "")
        sentencesCount= st.slider('Select sentence count', 3, 10 , value = 3)
        st.write("The above text will be summarized into {sentencesCount} sentences.".format(sentencesCount=sentencesCount))
        if st.button("Okay, Generate Summary"):
                st.caption("Using the sumy automatic summarizer module........")
                st.success("The summary result is:")
                st.write(summarizer(InputText , sentencesCount))

    #Sentiment Analysis
    elif task == "Detect Sentiment":
        InputText = st.text_area("Paste the message that you want to analyze here.", "")
        if st.button("Detect Sentiment"):
            st.success("The sentiment results of the above message is:")
            st.write(sentiment(InputText))
    
    else:
        st.subheader("Nothing to do here!")
        st.write("Please select an action from the dropdown menu.")


    st.sidebar.subheader("Developed happily by")
    st.sidebar.text("Prakriti Regmi :) ")
    st.sidebar.write("Visit me on :")
    st.sidebar.write("[Github](https://github.com/prakriti42)")
    st.sidebar.info("Happy Streamlit-ing!")

   
    # with st.container():  
    #     if st.button("Refresh Page"):
    #         pyautogui.hotkey("ctrl","F5")
           # st.legacy_caching.clear_cache()
           
           

if __name__ == '__main__':
    main()
