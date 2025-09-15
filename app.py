from flask import Flask, render_template, request
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def index():
    return "<a href='/signup'>Sign up</a><br><a href='/signin'>Log in</a>"


@app.route("/signup", methods=['GET', 'POST'])
def signup(name=None):
    if request.method == 'POST':
        # handle the signup logic here
        print(request.form.get('email'))
        return show_user(request.form.get('email'))
    return render_template('signup.html', name=name)


@app.route('/user/<string:user_id>')
def show_user(user_id):
    # show the user with the given id, the id is an integer
    return f'User {user_id}'


@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        return show_user(request.form.get('email'))
    return render_template('signin.html')


if __name__ == '__main__':
    app.run(debug=True)