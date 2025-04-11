import pandas as pd

def load_messages(path="data/sample_messages.csv"):
    df = pd.read_csv(path)
    return df['message'].tolist()
