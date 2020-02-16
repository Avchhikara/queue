from flask import Flask, render_template
from connect import PostgresDB


app = Flask(__name__)


@app.route('/')
def home():
    # string = ""
    # with PostgresDB as cursor:
    #     cursor.execute("Select * from test")
    #     string = cursor.fetchall()
    # return string
    return render_template('home.html')


@app.route("/add")
def add():
    # Will add the job to the queue table only
    # string = ""
    # with PostgresDB as cursor:
    #     cursor.execute("Select * from test")
    #     string = cursor.fetchall()
    # return string
    return "This is the add page"


if __name__ == "__main__":
    app.run(debug=True)


with PostgresDB() as cursor:
    cursor.execute("Select * from test")
    string = cursor.fetchall()
print(string)
