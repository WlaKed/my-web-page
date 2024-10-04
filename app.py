# import Flask

from flask import Flask, render_template
import os # importing operating system module
from collections import Counter

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/text_analyzer')
def text_analyzer():
    return render_template('text_analyzer.html')


if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host = '0.0.0.0', port = port)

def analyze_text (text):
    words = text.split()
    total_number_of_words = len(words)
    number_of_characters = len(text)
    counter_of_words = Counter(words)
    most_common_word = counter_of_words.most_common(1)
    return most_common_word





