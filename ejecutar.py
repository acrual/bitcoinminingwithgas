from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, FloatField,
                    RadioField, SelectField, TextField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class SimpleForm(FlaskForm):
    hashratevariation = FloatField('What hash rate increase do you expect?', validators=[DataRequired()])
    btcpricevariation = FloatField('What btc price increase do you expect?', validators=[DataRequired()])
    numminers = FloatField('How many miners will you have?', validators=[DataRequired()])
    miningyield = FloatField('Mining yield?', validators=[DataRequired()])
    submit = SubmitField('Calculate')


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
        session['hashratevariation'] = form.hashratevariation.data
        session['btcpricevariation'] = form.btcpricevariation.data
        session['numminers'] = form.numminers.data
        session['miningyield'] = form.miningyield.data
        flash(f"You just changed your site data to: {session['hashratevariation'], session['btcpricevariation'], session['numminers'], session['miningyield']}")
        return redirect(url_for('index'))

    return render_template('index.html', form=form)

""" @app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html') """

if __name__ == "__main__":
    app.run(debug=True)