import random

from flask import Flask

app = Flask(__name__)

rand_value = random.randint(0,9)

@app.route("/<int:number>")
def guess(number):
    if number < rand_value:
        return '<h1>too Low!</h1>'
    if number > rand_value:
        return '<h1>too High!</h1>'
    return '<h1>Correct!</h1>'


@app.route("/")
def root():
    return '<h1>Guess a number between 0 and 9</h1>' \
            f'<img src="/static/number.gif" alt="Number Image"> '



if __name__ == "__main__":
    app.run(debug=True)