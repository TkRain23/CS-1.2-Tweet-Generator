from flask import Flask
from sampling import weighted_random

app = Flask(__name__)

histogram = eval(open('histogram.txt', 'r').read())


def hello():
    return "Hello World!"


@app.route("/")
def sentence_generator():
    sentence = []

    for i in range(10):
        word = weighted_random(histogram)
        sentence.append(word)

    return " ".join(sentence)
