# logic of the application
from app import app
from flask import render_template

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

