from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'my_secret_key'

users = {}

chat_history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'register' in request.form:
            username = request.form['username']
            password = request.form['password']
            if len(username) < 3 or len(password) < 3:
                return render_template('index.html', message='too short login or password')
            if username in users:
                return render_template('index.html', message='username already exist')
            users[username] = password
            session['username'] = username
            return redirect('/chat')
        elif 'login' in request.form:
            username = request.form['username']
            password = request.form['password']
            if username in users and users[username] == password:
                session['username'] = username
                return redirect('/chat')
            else:
                return render_template('index.html', message='wrong username or password')
    return render_template('index.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'username' not in session:
        return redirect('/')
    if request.method == 'POST':
        message = request.form['message']
        username = session['username']
        chat_history.append((username, message))
    return render_template('chat.html', username=session['username'], chat_history=chat_history)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


app.run()