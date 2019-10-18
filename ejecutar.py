from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, FloatField,
                    RadioField, SelectField, TextField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class GensetForm(FlaskForm):
    gensetYesNo = SelectField(choices=[(1,"Yes, I will use a Genset"),(2,"No, I will directly plug to the electricity")]) 
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
    submit = SubmitField('Calculate')

@app.route('/', methods=['GET','POST'])
def index():
    form2 = GensetForm()
    if form2.validate_on_submit():
        session['gensetYesNo'] = form2.gensetYesNo.data
        if session['gensetYesNo'] == 1:
            return redirect(url_for('siteFormGas'))
        else:
            return redirect(url_for('siteFormNoGas'))
    return render_template('index.html', form2=form2)
    
@app.route('/siteFormGas', methods=['GET', 'POST'])
def siteFormGas():
    form = GasForm()
    if form.validate_on_submit():
        session['hashratevariation'] = form.hashratevariation.data
        session['btcpricevariation'] = form.btcpricevariation.data
        session['numminers'] = form.numminers.data
        session['miningyield'] = form.miningyield.data
        session['date'] = form.date.data
        session['savings'] = form.savings.data
        flash(f"You just changed your site data to: {session['hashratevariation'], session['btcpricevariation'], session['numminers'], session['miningyield']}")
        return redirect(url_for('index'))
    return render_template('siteFormGas.html', form=form)

@app.route('/siteFormNoGas', methods=['GET', 'POST'])
def siteFormNoGas():
    form = NoGasForm()
    if form.validate_on_submit():
        session['hashratevariation'] = form.hashratevariation.data
        session['btcpricevariation'] = form.btcpricevariation.data
        session['numminers'] = form.numminers.data
        session['miningyield'] = form.miningyield.data
        session['date'] = form.date.data
        session['savings'] = form.savings.data
        flash(f"You just changed your site data to: {session['hashratevariation'], session['btcpricevariation'], session['numminers'], session['miningyield']}")
        return redirect(url_for('index'))
    return render_template('siteFormNoGas.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)