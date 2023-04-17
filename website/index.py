from flask import Flask, render_template
# from ukrajinet_data import 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/Ukrajinet/')
def view_ukrajinet():
    return render_template('ukrajinet.html',
                            uk_wordnet = queries.cuisine_worldwide())

if __name__ == '__main__':
    app.run(debug = True)

