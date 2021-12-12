#controller handles routing and calls functions defined in models
import re
from flask_app import app # refers to __init__.py I think
from flask import render_template, redirect, request
from flask_app.models.user_model import User

@app.route('/')
def go_home():
    return render_template('home.html')

@app.route('/read')
def read_users():
    all_users = User.get_all_users()
    return render_template('read.html', all_users = all_users)

@app.route('/add_user')
def add_new_user():
    return render_template('add_user.html')

@app.route('/user/create', methods = ['POST'])
def created_new_user():
    new_user = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    User.add_new_user(new_user)
    return redirect('/')

#select cols you want to see, from where, if you do have to do a join how do you do it, condition