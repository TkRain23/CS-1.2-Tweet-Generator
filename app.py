# main script, uses other modules to generate sentences

from flask import Flask, render_template
# from stochastic_sampling import weighted_random
import markov
import re

app = Flask(__name__)

app.markov = markov.main()

histogram = eval(open('histogram.txt', 'r').read())


def hello():
    """
    """
    return "Hello World!"


@app.route("/")
def sentence_generator():
    """
    """
    final_sentence = app.markov.create_sentence()
    # " ".join(final_sentence.split(r'(.+|!++)')[:-1])

    return render_template("main.html", sentence=final_sentence)
