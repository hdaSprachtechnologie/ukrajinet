from flask import Flask, render_template
import ukrajinet

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                            uk_wordnet = ukrajinet.get_word_dict())

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/login/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug = True)

