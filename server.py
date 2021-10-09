from login import username
from flask import Flask, render_template

app = Flask('Login_System')


@app.route('/')
def index():
    return render_template('index.html', username=username)


app.run()