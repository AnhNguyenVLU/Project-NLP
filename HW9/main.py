import torch
from transformers import pipeline
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import pandas as pd

app = Flask(__name__)
app.config.update(
    SECRET_KEY='mykey',
    UPLOAD_FOLDER='static/files'
)

class MyForm(FlaskForm):
    text = StringField('Type something', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template("index.html")

checkpoints = "Lab9"
pipe = pipeline("text-generation", max_length=30, pad_token_id=0, model=checkpoints)

@app.route('/lab9', methods=['GET', 'POST'])
def storygenerator():
    form = MyForm()
    gen = False
    text = False
    print(form.validate_on_submit())
    if form.validate_on_submit():
        text = form.text.data 
        gen = pipe(text)[0]["generated_text"]
        print(gen)
        form.text.data = ""
    return render_template("lab9.html", form=form, text=text, gen=gen)

if __name__ == "__main__":
    app.run(debug=True)
