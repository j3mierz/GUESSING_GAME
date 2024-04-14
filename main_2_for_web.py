# reversed guessing game for web app

from flask import Flask, render_template, request

app = Flask(__name__)


def computer_next_number(a, b):
    return int((b - a) / 2 + a)


@app.route('/', methods=['GET', 'POST'])
def reversed_guessing_game():
    if request.method == 'GET':
        return render_template('guessing_game_form.html', min=1, max=1000, guess=500)
    if request.method == "POST":
        max = int(request.form.get('max'))
        min = int(request.form.get('min'))
        guess = int(request.form.get("guess", 500))
        user_answer = request.form.get('user_answer')

        if user_answer == 'too small':
            min = guess
        if user_answer == 'too big':
            max = guess
        elif user_answer == 'you won':
            return render_template('guessing_game_form.html', guess=guess, min=min, max=max, message='I won')
        guess = computer_next_number(max, min)

        return render_template('guessing_game_form.html', guess=guess, min=min, max=max)
