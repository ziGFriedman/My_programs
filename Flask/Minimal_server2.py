from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/test')
@app.route('/test2')
def home2():
    return 'Hello User!'

if __name__ == '__main__':
    app.run()
