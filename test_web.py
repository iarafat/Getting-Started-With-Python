from flask import Flask

from hs_student import HighSchoolStudent

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello World!'


@app.route("/about")
def about():
    return 'This is about page for this website'


@app.route("/student")
def student():
    hs = HighSchoolStudent('james')
    return hs.get_school_name()


if __name__ == '__main__':
    app.run()





















