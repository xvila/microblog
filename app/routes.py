# logic of the application
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/index')# you can chain routes
@app.route('/') # associate the top level url with this function
def index():
    user = {'username':'xavier'}
    posts = [
        {
            'author':{'username':'Xavier'},
            'body':'Beautiful day in NYC'
        },
        {
            'author':{'username':'Argyle'},
            'body':'Can\'t wait for avengers endgame'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts) 


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

# url_for builds a url for a specific function. So rather than manually typing in a url such as '/index' you can type 
# url_for(index) to generate the links. index is the name of the function such as def index():