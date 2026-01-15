from app import app
from flask import render_template, request, redirect, url_for
from flask_login import (
    current_user, login_user, logout_user, login_required
)
from app import alquimias

@app.route('/')
@login_required
def index():
    posts = alquimias.get_timeline()
    return render_template('index.html', user=current_user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        user = alquimias.validate_user_password(
            request.form['username'].lower(),
            request.form['password'].lower()
        )
        if user:
            login_user(user, remember=user.remember)
            return redirect(url_for('index'))
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        user = alquimias.create_user(
            username=request.form['username'].lower(),
            password=request.form['password'].lower(),
            remember=True if request.form.get('remember') else False,
            foto=request.form['foto'],
            bio=request.form['bio']
        )
        login_user(user)
        return redirect(url_for('index'))

    return render_template('cadastro.html')

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        alquimias.create_post(request.form['body'], current_user)
        return redirect(url_for('index'))
    return render_template('post.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
