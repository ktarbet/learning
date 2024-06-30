import datetime
import requests
from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def root():
    random_number = random.randint(1, 10)
    args = {"num": random_number, "year": datetime.datetime.now().year}
    return render_template('index.html', args=args)

def getAge(name):
    url = f"https://api.agify.io/?name={name}"
    res = requests.get(url)
    print(res.json())
    return res.json()["age"]

def getGender(name):
    url = f"https://api.genderize.io?name={name}"
    res = requests.get(url)
    return res.json()["gender"]

@app.route("/blog/<num>")
def blog(num):
    print(num)
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(url).json()
    return render_template("blog.html",posts=all_posts)

@app.route("/guess/<name>")
def guess(name):
    age = getAge(name)
    gender = getGender(name)
    return render_template("guess.html",name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
