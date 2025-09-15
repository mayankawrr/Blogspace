from flask import render_template, flash, redirect, url_for
from blogspace import app
from blogspace.forms import LoginForm

@app.route('/', endpoint='index')
@app.route('/index', endpoint='index')
def index():
    user = {'username': 'Mayank'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        } 
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    form = LoginForm()
    if form.validate_on_submit(): #returns true if request = post and server side validation is approved
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
        # here I could've have used render template, but that uses the same request, url will be login and re post, and it will resubmit form values, so use redirect only
    return render_template('login.html', title='Sign In', form=form) #form=form is done to pre load username and password in form re render when validation or request fails one time
# If you manually code the HTML form (without using Flask-WTF or a form object (jinja template rendering basically)), then form=form is not required in render_template