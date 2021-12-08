from LoanPrediction.model import User
from flask import render_template, url_for,request, flash,redirect,session,logging,request
from LoanPrediction.forms import RegistrationForm, LoginForm
from sqlalchemy import Column, Integer, String
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Mail, Message
import smtplib

from LoanPrediction import app, db, bcrypt, mail
import LoanPrediction.view as var
import _pickle as pickle
import json
import test
import os,inspect


file_name = inspect.getfile(inspect.currentframe())
path_name=os.path.dirname(os.path.abspath(file_name))

pred_model = pickle.load(open(path_name+'/trainedModel.sav','rb'))



@app.route("/")
@app.route("/home",methods=['GET','POST'])
@login_required
def home():
	'''if request.method == 'POST':
		comment = request.form['comments']
		sender_id = request.form['sender']
		msg = Message('Hello', sender='abc@gmail.com', recipients=['beproject2k19@gmail.com'])
		mail.send(msg)
		flash('Message Sent!')'''
	

	return render_template('MainLayout.html', title='Home')

@app.route("/register", methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, bank_name=form.bank_name.data , email_addr=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register',form=form)
     


@app.route("/login", methods=['GET','POST'])
def login():
		form = LoginForm()
		if form.validate_on_submit():
			user = User.query.filter_by(email_addr=form.email.data).first()
			if user and bcrypt.check_password_hash(user.password, form.password.data):
				login_user(user, remember=form.remember.data)
				next_page = request.args.get('next')
				return redirect(next_page) if next_page else redirect(url_for('home'))	
			else:
				flash('Login Unsuccessful. Please check email and password', 'danger')

		return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))




@app.route("/view", methods=['GET','POST'])
@login_required
def view():
	if request.method == 'GET':
		return render_template('view.html', title='View')
	elif request.method == 'POST':
		info = var.search_cid(request.form['cid'])
		if isinstance(info,str) :
			flash(info, 'danger')
			return redirect(url_for('view'))
		label = var.attr()
		data = {}
		for i in range(len(label)):
			data[label[i]] = info[i+1]
		return render_template('view.html', data=data)
			



@app.route("/analyze")
@login_required
def analyze():
	data = pred_model.feature_importances_
	data = [round(x*100,2) for x in data]
	labels = var.labels()
	table_data = zip(labels,data)
	return render_template('analyze.html',data = data,labels = json.dumps(labels),table_data = table_data)

@app.route("/generate",methods=['GET', 'POST'])
@login_required
def generate():
	if request.method == 'GET':
		return render_template('generate.html', title='Generate')
	if request.method == 'POST':
		form = request.form
		attribut = []
		attribut.append(float(form['amount']))
		attribut.append(float(form['cscore']))
		attribut.append(float(form['annualincome']))
		attribut.append(float(form['monthlydebt']))
		attribut.append(float(form['yearsofhistory']))
		attribut.append(float(form['openacc']))
		attribut.append(float(form['creditbalance']))
		attribut.append(float(form['maxopencredit']))
		val = pred_model.predict_proba([attribut])[0]
		data = []
		data.append(val[1])
		data.append(val[0])
		labels =[]
		labels.append(str(data[0]))
		labels.append("")
		print(data)
		# return render_template('score.html',data=data)
		if data[0] >= 0.5:
			flash("Score cleared the threshold hence loan can be granted","success")
		else:
			flash("Score did not clear the threshold hence loan cannot be granted","danger")
		return render_template('score.html',data = data,labels = json.dumps(labels))
