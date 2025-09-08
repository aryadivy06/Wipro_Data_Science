import pandas as pd
import string
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

from nltk.corpus import stopwords

df = pd.read_csv("SMSSpamCollection", sep='\t', names=["label", "message"])

print("Sample data:\n", df.head())


stop_words = set(stopwords.words("english"))

def preprocess_text(text):
  
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
  
    tokens = [word for word in tokens if word not in stop_words]
   
    return " ".join(tokens)

# Apply preprocessing
df["cleaned"] = df["message"].apply(preprocess_text)

print("\nPreprocessed sample:\n", df[["message", "cleaned"]].head())


X_train, X_test, y_train, y_test = train_test_split(
    df["cleaned"], df["label"], test_size=0.2, random_state=42
)

# Convert text → TF-IDF features
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


model = MultinomialNB()
model.fit(X_train_tfidf, y_train)


y_pred = model.predict(X_test_tfidf)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification report:\n", classification_report(y_test, y_pred))
