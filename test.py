import os
import numpy as np
import pandas as pd
import urllib.request as requests
import string
import re
from wordcloud import WordCloud
from collections import Counter
import unicodedata
import regex as re
import joblib
from pyvi import ViTokenizer, ViPosTagger
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
folder_path = os.path.join(base_dir, 'dataset')

model_path = os.path.join(folder_path, 'vietnamese-stopwords.txt')
stop_words = []
with open('dataset/vietnamese-stopwords.txt', encoding='utf-8') as f:
    stop_words = [t for t in f.read().split('\n')]

vocab_size = 5000
embedding_dim = 64
max_length = 30
data = pd.read_csv('dataset/output.csv')
sequences = data['processed'].fillna('')
sequences = sequences.astype(str)

tokenizer = Tokenizer(num_words=vocab_size, oov_token='<OOV>')
tokenizer.fit_on_texts(sequences)


sequencePattern   = r"(.)\1\1+"
seqReplacePattern = r"\1"

# Defining regex for emojis
smile_emoji        = r"[8:=;]['`\-]?[)d]+"
sad_emoji          = r"[8:=;]['`\-]?\(+"
neutral_emoji      = r"[8:=;]['`\-]?[\/|l*]"

def preprocess(input:str):
    if isinstance(input, str):
      input = unicodedata.normalize('NFC', input)

      # Lower
      input = input.lower()
      # clean
      input = input.strip().replace('\n', '')

      input = re.sub(sequencePattern, seqReplacePattern, input)

      # Replace all emojis.
      input = re.sub(r'<3', 'tim', input)
      input = re.sub(smile_emoji, 'vui', input)
      input = re.sub(sad_emoji, 'buồn', input)
      input = re.sub(neutral_emoji, 'bình thường', input)

      # Keep word
      input = re.sub('https?://\S+|www\.\S+', ' ', input)
      input = re.sub('[%s]' % re.escape(string.punctuation), ' ', input)

      input = ViTokenizer.tokenize(input)

      return ' '.join([word for word in input.split() if word not in stop_words])
    else:
      return ''
    
model = load_model('dataset/model.h5')

def my_predict(input:list):
    input = [preprocess(i) for i in input]
    text_tokenizer = tokenizer.texts_to_sequences(pd.Series(input))
    padded_test = pad_sequences(text_tokenizer, maxlen=max_length, truncating='post', padding='post')
    y_predict = model.predict(padded_test)
    for t, pred in zip(input, y_predict):
        print(f'{t} : {sentiment(pred)} ({pred.round(decimals=3)})')

def sentiment(x:int):
    if x > 0.6:
        return 'positive'
    if x > 0.4:
        return 'neutral'
    return 'negative'

my_predict(['ok'])