import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = [ps.stem(i) for i in text if i.isalnum() and i not in stopwords.words('english') and i not in string.punctuation]
    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.set_page_config(page_title="Spam Classifier", page_icon="📧")
st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message", height=150)

col1, col2 = st.columns(2)

with col1:
    if st.button('Predict'):
        if input_sms.strip() == "":
            st.warning("Please enter a message first!")
        else:
            # 1. preprocess
            transformed_sms = transform_text(input_sms)
            # 2. vectorize
            vector_input = tfidf.transform([transformed_sms])
            # 3. predict
            result = model.predict(vector_input)[0]
            
            # 4. Display
            if result == 1:
                st.error("🚨 This is SPAM")
            else:
                st.success("✅ This is NOT SPAM (Ham)")

with col2:
    if st.button('Clear Input'):
        st.rerun() # This refreshes the app and clears the text area