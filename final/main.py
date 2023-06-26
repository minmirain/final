import datetime
import time
import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    sentence = get_random_sentence()
    return render_template('index.html', sentence=sentence, start_time=datetime.datetime.now().timestamp())

@app.route('/', methods=['POST'])
def result():
    start_time = float(request.form['start_time'])
    sentence = request.form['sentence']
    typed_text = request.form['typed_text']
    end_time = time.time()
    typing_time = round(end_time - start_time, 2)
    accuracy = calculate_accuracy(sentence, typed_text)
    wpm = calculate_wpm(typed_text, typing_time)
    cpm = calculate_cpm(typed_text, typing_time)

    return render_template('result.html', typing_time=typing_time, accuracy=accuracy, wpm=wpm, cpm=cpm)

def get_random_sentence():
    sentences = [
        "The seconds are relentless,            "
        "I'm helpless as they keep flying by.           "
        "Stuck here in the desert,                      "
        " I feel like I'm in an hourglass. "
        "Maybe I can stay and be comfortable living in the past. "
        "But I don't wanna be alone so can you take me to you now. ",
        "So many thoughts are inside of my head "
        "I'm always drying these tears on my face. "
        "How could I ever get used to the fact               ."
        "That the songs and the lyrics, they all sound the same. ",
        "Ayy, domino, flick and a drop and I see it all fall down. "
        "Shakin’ the world, magnitude makin' everything crumble like blah, blah. "
        "Okay, all that's left is dust, A.K.A. The Bulldozer. "
        "Right when everyone falls, they're crawling ’cause they can't help but follow. ",
        "Setting up my ambitions, Check 'em one at a time, yeah, I made it. "
        "Now it's time for ignition I'm the start, heat it up. "
        " They follow, burning up a chain reaction, oh, oh, oh. ",
        " I know that feeling too, I've been inside the dark, "
        "I've never been so empty, hopeless "
        "(You are) But no, it isn't true. "
        "Cause know that all the stars are by your side. ",
        "You know, whenever there's a chance I will tell you that you're amazing as you are. "
        "Cause when you give me a glance I am sure that I see the universe in your eyes. "
        "Don't you ever tell yourself that you're not enough I am certain that you're truly fine. "

    ]
    return random.choice(sentences)

def calculate_accuracy(sentence, typed_text):
    correct_chars = sum(a == b for a, b in zip(sentence, typed_text))
    accuracy = (correct_chars / len(sentence)) * 100
    return round(accuracy, 2)

def calculate_wpm(typed_text, typing_time):
    words = typed_text.split()
    num_words = len(words)
    minutes = typing_time / 60
    wpm = num_words / minutes
    return round(wpm, 2)

def calculate_cpm(typed_text, typing_time):
    num_chars = len(typed_text)
    minutes = typing_time / 60
    cpm = num_chars / minutes
    return round(cpm, 2)


if __name__ == '__main__':
    app.run(debug=True)
