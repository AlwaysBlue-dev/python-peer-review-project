""""Import package & required libraries"""
import machine_translation
from flask import Flask

app = Flask("Translation Web App")


@app.route("/")
def index():
    return "IBM WATSON LANUAGE TRANSLATOR"


@app.route("/englishToFrench")
def e2f():
    return machine_translation.translator.english_to_french("Hello")


@app.route("/frenchToEnglish")
def f2e():
    return machine_translation.translator.french_to_english("Bonjour")


if __name__ == "__main__":
    app.run(debug=True)
    # When no port is specified, starts at deault port 5000
