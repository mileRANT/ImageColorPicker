from flask import Flask, render_template, request

app = Flask(__name__)


# function to evaluate the file sent


def give_most_hex(file):
    pass


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)