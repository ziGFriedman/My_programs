from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/test')
@app.route('/test2')
def home2():
    return 'Hello User!'

@app.route('/hello/<user>')    # <str:user> по умолчанию все аргументы str (Передает аргумент user в url пути)
def home3(user):
    return 'Hello, User: ' + user

if __name__ == '__main__':
    app.run()
