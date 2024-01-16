"""app.py flask application to translate text from english to spanish"""
from flask import Flask, request, render_template
from dotenv import load_dotenv
from translator import translate_input, translation_model

load_dotenv()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    original_text = request.form['text']
    target_language = request.form['language']
    print(original_text, target_language)
    # Retrieve the translation
    translated_text = translate_input(
        translation_model, source_text=original_text)

    # Call render template, passing the translated text,
    # original text, and target language to the template
    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language
    )
