import re
import pandas as pd
from nltk.translate import AlignedSent, IBMModel1

df = pd.read_csv("./data/engspn.csv")


def clean_sentences(sentences):
    cleaned_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        sentence = sentence.lower()
        sentence = re.sub(r"[^a-zA-Z0-9]+", " ", sentence)
        cleaned_sentences.append(sentence.strip())
    return cleaned_sentences


english_sentences = df["english"].tolist()
spanish_sentences = df["spanish"].tolist()
cleaned_english_sentences = clean_sentences(english_sentences)
cleaned_spanish_sentences = clean_sentences(spanish_sentences)


def train_translation_model(source_sentences, target_sentences):
    aligned_sentences = [
        AlignedSent(source.split(), target.split())
        for source, target in zip(source_sentences, target_sentences)
    ]
    ibm_model = IBMModel1(aligned_sentences, 10)
    return ibm_model


translation_model = train_translation_model(
    cleaned_english_sentences, cleaned_spanish_sentences
)


def translate_input(ibm_model, source_text):
    cleaned_text = clean_sentences(source_text.split())
    source_words = cleaned_text
    translated_words = []
    for source_word in source_words:
        max_prob = 0.0
        translated_word = None
        for target_word in ibm_model.translation_table[source_word]:
            prob = ibm_model.translation_table[source_word][target_word]
            if prob > max_prob:
                max_prob = prob
                translated_word = target_word
        if translated_word is not None:
            translated_words.append(translated_word)
    translated_text = " ".join(translated_words)
    return translated_text
