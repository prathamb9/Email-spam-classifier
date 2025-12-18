# 📧 Email/SMS Spam Classifier

An end-to-end Machine Learning web application that classifies messages as **Spam** or **Ham** (Not Spam) using Natural Language Processing (NLP).

## 🚀 Live Demo
**[Click here to try the App!](https://email-spam-classifier-5l6r.onrender.com/)** *(Note: On the free tier, the first load may take 1-2 minutes to wake up the server.)*

---

## 🛠️ Project Components
- **`app.py`**: Streamlit web interface and classification logic.
- **`Spam_detector.ipynb`**: Jupyter Notebook containing Data Cleaning, EDA, and Model Training logic.
- **`spam.csv`**: The raw dataset used for training the model.
- **`model.pkl` & `vectorizer.pkl`**: The saved weights for the Naive Bayes model and TF-IDF vectorizer.

## ⚙️ Technical Workflow
1. **Preprocessing**: Text is lowercased and tokenized using NLTK.
2. **Cleaning**: Stopwords and punctuation are removed.
3. **Stemming**: Words are reduced to their root form using `PorterStemmer`.
4. **Vectorization**: Text is transformed into numerical vectors using `TfidfVectorizer`.
5. **Prediction**: A Multinomial Naive Bayes classifier predicts the final category.

## 🔧 Local Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/prathamb9/Email-spam-classifier.git](https://github.com/prathamb9/Email-spam-classifier.git)