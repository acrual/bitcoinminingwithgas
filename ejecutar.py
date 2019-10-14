from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                    RadioField, SelectField, TextField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class SimpleForm(FlaskForm):
    breed = StringField('What breed are you?', validators=[DataRequired()])
    submit = SubmitField('Change breed')

""" class InfoForm(FlaskForm):
    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField('Have you been neutered?')
    mood = RadioField('Please choose your mood: ',
                        choices=[('mood one', 'happy'),('mood two','Excited')])
    food_choice = SelectField(u'Pick your favourite food',
                            choices=[('chi','Chicken'),('bf','beef'),('fish','Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit') """

@app.route('/', methods=['GET','POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You just changed your breed to: {session['breed']}")
        return redirect(url_for('index'))

    return render_template('index.html', form=form)
    """ form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data   
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))

    return render_template('index.html', form=form) """

""" @app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html') """

if __name__ == "__main__":
    app.run(debug=True)