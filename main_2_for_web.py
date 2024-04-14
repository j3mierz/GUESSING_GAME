# reversed guessing game for web app

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def reversed_guessing_game():

    return render_template('guessing_game_form.html')
