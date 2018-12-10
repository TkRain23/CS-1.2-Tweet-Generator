# main script, uses other modules to generate sentences
from flask import Flask, render_template
# from stochastic_sampling import weighted_random
import markov
import re

app = Flask(__name__)

app.markov = markov.main()

@app.route("/")
def sentence_generator():
    """
    """
    final_sentence = app.markov.create_sentence()

    return render_template("main.html", sentence=final_sentence)
