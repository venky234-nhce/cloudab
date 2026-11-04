from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My Python Website!"

@app.route('/about')
def about():
    return "This is my About Page"

if __name__ == '__main__':
    app.run(debug=True)