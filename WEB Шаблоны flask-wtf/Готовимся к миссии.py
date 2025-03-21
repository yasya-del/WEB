from flask import Flask, url_for, request,  render_template, redirect
from loginform import LoginForm
from flask_wtf import FlaskForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)
@app.route('/training/<prof>')
def trainy(prof):
    return render_template('training.html', prof=prof)
@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_prof.html', list=list)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')