from flask import Flask, render_template, request
from markupsafe import escape
from flask_socketio import SocketIO, send, emit



app = Flask(__name__)

socketio = SocketIO(app)

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

@app.route('/chat', methods=['GET', 'POST'])
def message(name=None):
    chats=[]
    if request.method=='POST':
        handlemessage({ "usermessage":request.form.get("msg")})
    return render_template('message.html', name=name, chats=chats)

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        return show_user(request.form.get('email'))
    return render_template('signin.html')

@socketio.on('message')
def handlemessage(data):
    print("Current chats: ", data)
    emit("message", [data], boradcast=True)
  

@socketio.on('connect')
def handleConnect(user):
    print("User is connected: ", user)


if __name__ == '__main__':
    socketio.run(app, port=8080, debug=True, use_reloader=True)
    #app.run(debug=True)
