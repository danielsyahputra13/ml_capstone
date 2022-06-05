from fastapi import FastAPI
from pydantic import BaseModel

import tensorflow as tf
import json
import numpy as np
import pandas as pd
import translators as ts

from preprocess import SpacyPreprocessor
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder


spacy_model = SpacyPreprocessor.load_model()
preprocessor = SpacyPreprocessor(spacy_model=spacy_model, lemmatize=True, remove_numbers=True, remove_stopwords=True)

app = FastAPI()


class Teks(BaseModel):
    desc: str

@app.get("/")
async def root():
    return {"message": "Please, go to /docs endpoint for more info"}

@app.post("/predict/")
async def predict(teks: Teks):
    # Translate ke inggris
    translated_text = ts.google(teks.desc, to_language='en')

    # Preprocess
    desc_cleaned = preprocessor.preprocess_text(translated_text)

    # Predict
    with open('assets/tokenizer.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
   
    max_length = 100
    trunc_type = 'post'
    padding_type = 'post'

    pred_sequences = tokenizer.texts_to_sequences([desc_cleaned])
    pred_padded = pad_sequences(pred_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

    model = tf.keras.models.load_model('assets/model.h5')

    result = model.predict(pred_padded)[0]
    idx = result.argsort()[-3:][::-1]

    encoder = LabelEncoder()
    encoder.classes_ = np.load('assets/encoder.npy', allow_pickle=True)

    conditions = encoder.inverse_transform(idx)

    ############################################

    # load description and medicine
    description = pd.read_pickle("data/description.pkl")

    result_json = []
    for i in range(len(conditions)):
        condition = conditions[i]
        probability = float(result[idx[i]])
        deskripsi = description[description['Condition'] == condition]['Deskripsi'].values[0]
        result_json.append(
            {
                "disease": condition,
                "probability": probability,
                "deskripsi": deskripsi,
            }
        )

    return {
        "description": desc_cleaned,
        "result": result_json
    }