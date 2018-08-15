#!/usr/local/bin/python3
from flask import render_template
from flask import Flask,abort,Response
app = Flask(__name__)


@app.route("/")
def home():
	name="ganteng"
	return render_template('home.peuyeum', SignIn=True, SignUp=True)
	
@app.route("/process")
def process():
	name="ganteng"
	return render_template('process.peuyeum', SignIn=True, SignUp=True)

@app.route("/signin")
def signin():
	name="ganteng"
	return render_template('signin.peuyeum', SignIn=True, SignUp=True)

@app.route("/signup")
def signup():
	name="ganteng"
	return render_template('signup.peuyeum', SignIn=True, SignUp=True)

	


