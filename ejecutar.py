from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, FloatField,
                    RadioField, SelectField, TextField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired, InputRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class GensetForm(FlaskForm):
    gensetYesNo = RadioField(choices=[(int(1),"Yes, I will use a Genset"),(int(2),"No, I will directly plug to the electricity")], validators=[DataRequired()]) 
    submit = SubmitField('Submit')

class GasForm(FlaskForm):
    hashratevariation = FloatField('What hash rate increase do you expect?', validators=[DataRequired()])
    btcpricevariation = FloatField('What btc price increase do you expect?', validators=[DataRequired()])
    numminers = FloatField('How many miners will you have?', validators=[DataRequired()])
    miningyield = FloatField('Mining yield?', validators=[DataRequired()])
    date = DateTimeField('Date?', validators=[DataRequired()])
    savings = TextAreaField('Please explain briefly what the savings are all about', validators=[DataRequired()])
    submit = SubmitField('Calculate')

class NoGasForm(FlaskForm):
    hashratevariation = FloatField('What hash rate increase do you expect?', validators=[DataRequired()])
    btcpricevariation = FloatField('What btc price increase do you expect?', validators=[DataRequired()])
    numminers = FloatField('How many miners will you have?', validators=[DataRequired()])
    miningyield = FloatField('Mining yield?', validators=[DataRequired()])
    date = DateTimeField('Date?', validators=[DataRequired()])
    savings = TextAreaField('Please explain briefly what the savings are all about', validators=[DataRequired()])
    submit = SubmitField('Calculate2')

@app.route('/', methods=['GET','POST'])
def index():
    form = GensetForm()
    """ print(form.errors)
    print("pasa : ", int(session['gensetYesNo']) + 1)
    print(form.validate_on_submit())
    if int(session['gensetYesNo']) > 0: """
    session['gensetYesNo'] = form.gensetYesNo.data
    print("pasa esto otro: ", session['gensetYesNo'])
    if session['gensetYesNo'] == 1:
        return redirect(url_for('siteFormGas'))
    else:
        return redirect(url_for('siteFormNoGas'))
    return render_template('index.html', form=form)
    
@app.route('/siteFormGas', methods=['GET', 'POST'])
def siteFormGas():
    form2 = GasForm()
    if form2.validate_on_submit():
        session['hashratevariation'] = form2.hashratevariation.data
        session['btcpricevariation'] = form2.btcpricevariation.data
        session['numminers'] = form2.numminers.data
        session['miningyield'] = form2.miningyield.data
        session['date'] = form2.date.data
        session['savings'] = form2.savings.data
        flash(f"You just changed your site data to: {session['hashratevariation'], session['btcpricevariation'], session['numminers'], session['miningyield']}")
        return redirect(url_for('index'))
    return render_template('siteFormGas.html', form2=form2)

@app.route('/siteFormNoGas', methods=['GET', 'POST'])
def siteFormNoGas():
    form3 = NoGasForm()
    if form3.validate_on_submit():
        session['hashratevariation'] = form3.hashratevariation.data
        session['btcpricevariation'] = form3.btcpricevariation.data
        session['numminers'] = form3.numminers.data
        session['miningyield'] = form3.miningyield.data
        session['date'] = form3.date.data
        session['savings'] = form3.savings.data
        flash(f"You just changed your site data to: {session['hashratevariation'], session['btcpricevariation'], session['numminers'], session['miningyield']}")
        return redirect(url_for('index'))
    return render_template('siteFormNoGas.html', form3=form3)

if __name__ == "__main__":
    app.run(debug=True)