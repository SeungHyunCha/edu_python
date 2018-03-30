from flask import Flask

app = Flask(__name__) 

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

import random
com_num = random.randint(1,100)

@app.route('/guess/<int:user_num>')
def show_post(user_num):
    global com_num
    msg = ""
    if com_num == user_num:
        msg = "Good!!"
    elif com_num < user_num:
        msg = "Down!!"
    else:
        msg = "Up!!"
    return msg

if __name__ == '__main__':
    app.run(debug=True)