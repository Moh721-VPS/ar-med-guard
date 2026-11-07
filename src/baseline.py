import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

train = pd.read_csv("data/splits/train.csv")
test = pd.read_csv("data/splits/test.csv")

vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 5), min_df=2)
X_train = vec.fit_transform(train["text"])
X_test = vec.transform(test["text"])

clf = LogisticRegression(max_iter=1000, class_weight="balanced")
clf.fit(X_train, train["label_id"])

print("BASELINE (TF-IDF + LogReg)")
print(classification_report(test["label_id"], clf.predict(X_test),
                            target_names=["not_misleading", "misleading"]))
