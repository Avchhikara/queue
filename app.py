from flask import Flask, render_template, request
from add import Add


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route("/add", methods=['GET'])
def add():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add_post():
    val = Add(request)
    print(val.correct_data)
    if val.correct_data:
        return val.message, 200
    return val.message, 400


if __name__ == "__main__":
    app.run(debug=True)
