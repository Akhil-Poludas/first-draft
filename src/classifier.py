import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

def train():
    data = pd.read_csv("data/sample_messages.csv")
    data = pd.read_csv("data/sample_messages.csv")
    labels = [
    "Technical",          # internet not working
    "Billing/Payments",   # bill showing due
    "Sales/Upgrade",      # change plan
    "Technical",          # slow connection
    "Billing/Payments",   # invoice copy
    "Billing/Payments",   # UPI payment issue
    "Sales/Upgrade",      # upgrade to Gold
    "Technical",          # channels missing
    "Technical",          # disconnecting
    "Billing/Payments",   # charged twice
    "Sales/Upgrade",      # cancel subscription
    "Technical",          # device overheating
    "Account Update",     # change email
    "Account Update",     # OTP not received
    "Sales/Upgrade"       # family plan info
]


    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', MultinomialNB())
    ])
    pipeline.fit(data['message'], labels)
    joblib.dump(pipeline, "models/classifier.pkl")
    print("Model trained and saved to models/classifier.pkl")

if __name__ == "__main__":
    train()
