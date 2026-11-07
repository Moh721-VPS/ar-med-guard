import numpy as np
import pandas as pd
from datasets import Dataset
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
from transformers import (AutoTokenizer, AutoModelForSequenceClassification,
                          TrainingArguments, Trainer)

MODEL = "aubmindlab/bert-base-arabertv02"
tok = AutoTokenizer.from_pretrained(MODEL)

def load(path):
    df = pd.read_csv(path)[["text", "label_id"]].rename(columns={"label_id": "labels"})
    ds = Dataset.from_pandas(df)
    return ds.map(lambda b: tok(b["text"], truncation=True, max_length=128,
                                padding="max_length"), batched=True)

train, val, test = (load(f"data/splits/{s}.csv") for s in ["train", "val", "test"])

model = AutoModelForSequenceClassification.from_pretrained(MODEL, num_labels=2)

def metrics(p):
    preds = np.argmax(p.predictions, axis=1)
    pr, rc, f1, _ = precision_recall_fscore_support(p.label_ids, preds, average="binary", zero_division=0)
    return {"accuracy": accuracy_score(p.label_ids, preds),
            "precision": pr, "recall": rc, "f1": f1}

args = TrainingArguments(
    output_dir="outputs", num_train_epochs=4, per_device_train_batch_size=16,
    learning_rate=2e-5, eval_strategy="epoch", save_strategy="no",
    report_to="none", seed=42)

trainer = Trainer(model=model, args=args, train_dataset=train,
                  eval_dataset=val, compute_metrics=metrics)
trainer.train()

print("TEST SET RESULTS (AraBERT)")
print(trainer.evaluate(test))
