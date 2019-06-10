from flask import Flask
from flask import request

app = Flask(__name__)
app.confug(DEBUG=True, SECRET_KEY='some secret!')

@app.route('/', methods=['GET', 'POST'])
def home():
    raise ValueError('Test!')
    return 'Hello World!', 200

if __name__ == '__main__':
    app.run()
    
