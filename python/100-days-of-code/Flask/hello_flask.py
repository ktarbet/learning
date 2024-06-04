# https://flask.palletsprojects.com/en/3.0.x/quickstart/
# https://pypi.org/project/Flask/


from flask import Flask

app = Flask(__name__)


@app.route("/hello/")
def hello_world():
    return "<p>Hello, World!</p>" \
       '<p> more text </p>'


@app.route("/bye")
def bye():
    return "Bye. "

def make_bold(f):
    def b():
        rval = "<b>"
        rval += f()
        rval += "</b>"
        return rval
    return b
def make_emphasis(f):
    def e():
        rval = "<em>"
        rval += f()
        rval += "</em>"
        return rval
    return e

def make_underlined(f):
    def u():
        rval = "<u>"
        rval += f()
        rval += "</u>"
        return rval
    return u

def tag(f,html_tag):
    rval = f"<{html_tag}>"
    rval += f()
    rval += f"</{html_tag}>"


@app.route("/bold-bye")
@make_bold
@make_emphasis
@make_underlined
def bold_bye():
    #return "<u><em><b>Hi...</b></em></u>"
    return "with decorators"

@app.route("/username/<path:name>")
def greet(name):
    return f"hello: {name}"


# https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    app.run(debug=True)
