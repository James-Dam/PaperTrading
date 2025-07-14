from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy

app = Flask(__name__)
toolbar = DebugToolbarExtension(app)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = 'b04464d4af1ddfaa05582eef16047910'


@app.route('/')
@app.route('/home')
def home():
    username = request.args.get('username', 'James')
    return render_template('home.html', username=username)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home', username=form.username.data)) # if so - send to home page
    return render_template('register.html', title='Register', form=form)
    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)