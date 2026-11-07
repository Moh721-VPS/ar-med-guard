import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/labeled/claims.csv")
df = df[df["label"].isin(["misleading", "not_misleading"])].dropna(subset=["text"])
df["label_id"] = (df["label"] == "misleading").astype(int)
print(df["label"].value_counts())

train, temp = train_test_split(df, test_size=0.3, stratify=df["label_id"], random_state=42)
val, test = train_test_split(temp, test_size=0.5, stratify=temp["label_id"], random_state=42)

train.to_csv("data/splits/train.csv", index=False)
val.to_csv("data/splits/val.csv", index=False)
test.to_csv("data/splits/test.csv", index=False)
print(len(train), len(val), len(test))
