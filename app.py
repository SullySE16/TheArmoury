from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, TextAreaField, IntegerField, BooleanField, RadioField, DateTimeField
from wtforms.validators import InputRequired, Length
from wtforms_validators import Alpha
import os
from flask_sqlalchemy import SQLAlchemy




basedir = os.path.abspath(os.path.dirname(__file__))





app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class SignUpForm(FlaskForm):
	firstname = StringField('First Name', validators=[InputRequired()])
	lastname = StringField('Last Name', validators=[InputRequired(), ])
	email = EmailField('Email', validators=[InputRequired()])
	username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=8,max=80)])
	submit = SubmitField('Submit')


class LoginForm(FlaskForm):

	username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
	submit = SubmitField('Submit')


@app.route('/login', methods= ['GET','POST'])
def login():

	form = LoginForm()

	if form.validate_on_submit():
		session['Username'] = form.username.data
		session['Password'] = form.password.data

		return redirect(url_for('homepage1.html', form=form))


	return render_template('login.html', form=form)


@app.route('/signup', methods= ['GET','POST'])
def signup():
	form = SignUpForm()

	if form.validate_on_submit():

		
		session['First Name'] = form.firstname.data
		session['Last Name'] = form.lastname.data
		session['Email'] = form.email.data
		session['Username'] = form.username.data
		session['Password'] = form.password.data
		
		
		

		return redirect(url_for('signedup', form=form))

	return render_template('signup.html',form=form)

	

@app.route('/homepage1')
def homepage():
	user_loggedin = True
	return render_template('Homepage1.html', user_loggedin=user_loggedin)

@app.route('/signedup')
def signedup():

	form=SignUpForm()
	
	flash("Sign Up Successful!")

	return render_template('signedup.html', form=form)

@app.route('/machineguns')
def machine_guns():
	return render_template('MachineGuns.html')

@app.route('/pistols')
def pistols():
	return render_template('Pistols.html')

@app.route('/rifles')
def rifles():
	weapons = ['SA80', 'C8', 'Sharpshooter']
	return render_template('Rifles.html', weapons=weapons)

@app.route('/smgs')
def smgs():
	return render_template('SMG.html')

@app.route('/snipers')
def snipers():
	return render_template('snipers.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


if __name__ == '__main__': 
	app.run(debug=True)

