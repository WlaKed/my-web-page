from flask import Flask, render_template, request
import os
from collections import Counter

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')

@app.route('/text_analyzer')
def text_analyzer():
    return render_template('text_analyzer.html')

@app.route('/analyze', methods=['POST'])  # Correctly handle the form submission
def analyze():
    text = request.form['text_to_analyze']
    analysis = analyze_text(text)
    return render_template('results.html', analysis=analysis)

def analyze_text(text):
    words = text.split()
    total_number_of_words = len(words)
    number_of_characters = len(text)
    counter_of_words = Counter(words)
    most_common_word = counter_of_words.most_common(1)[0] if words else ("None", 0)
    word_frequencies = sorted(counter_of_words.items(), key=lambda item: (-item[1], item[0]))
    
    return {
        'total_words': total_number_of_words,
        'total_characters': number_of_characters,
        'most_common_word': most_common_word,
        'word_frequencies': word_frequencies
    }

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
