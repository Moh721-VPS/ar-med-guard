# AR-MED Guard

AI detection of Arabic misinformation about unproven stem cell therapies.

## Goal
Build a labeled dataset of 200-500 real Arabic claims about stem cell treatments, fine-tune an Arabic NLP model (AraBERT), and test whether domain-specific training improves detection on unseen claims.

## Pipeline
1. Collect claims -> `data/raw/`
2. Label them following `docs/labeling_guide.md` -> `data/labeled/claims.csv`
3. Split (train/val/test) -> `python src/prepare_data.py`
4. Baseline (TF-IDF + logistic regression) -> `python src/baseline.py`
5. Fine-tune AraBERT -> `python src/train.py` (run on Google Colab GPU)
6. Final evaluation on held-out test set only

## Run on Google Colab
```python
!git clone https://github.com/YOUR_USERNAME/ar-med-guard.git
%cd ar-med-guard
!pip install -r requirements.txt
!python src/prepare_data.py
!python src/baseline.py
!python src/train.py
```

## Data rules
- Public content only. No private WhatsApp messages.
- Remove usernames, phone numbers and any personal information.
- The test set is never used for training or tuning.

## Future work
Arabic speech-to-text + classifier for forwarded voice notes.

## Team
See the Issues tab for task ownership.

## Quick demo (pipeline test only)
`data/demo/synthetic_demo.csv` has 40 synthetic examples (flagged `synthetic`) so the pipeline can be run end to end before real data exists. Do NOT mix them into `claims.csv` or report results from them.
Open `notebooks/01_run_pipeline.ipynb` in Google Colab to run everything.
