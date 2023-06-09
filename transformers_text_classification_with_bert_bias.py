# -*- coding: utf-8 -*-
"""Transformers - Text classification with BERT: bias.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/LinkedInLearning/transformers-text-classification-for-nlp-using-bert-2478096/blob/main/Transformers_Text_classification_with_BERT_bias.ipynb

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Yj5dWp0YoIaphOCXNr58fXkdGAnjkha8?usp=sharing)

# Bias in BERT
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install transformers[sentencepiece]

from transformers import pipeline

fill_mask = pipeline("fill-mask", model="bert-base-uncased")
results = fill_mask("The nurse needed a drink because [MASK] was tired after a long day's work at the hospital.")
results

results = fill_mask("The doctor needed a drink because [MASK] was tired after a long day's work at the hospital.")
results

results = fill_mask("We had a meeting with our company receptionist and [MASK] was not happy.")
results

results = fill_mask("We had a meeting with our company president and [MASK] was not happy.")
results

results = fill_mask("The programmer stepped away from the computer because [MASK] wanted a break.")
results