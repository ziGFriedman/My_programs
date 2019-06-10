from flask import Flask
from flask import request
import os

app = Flask(__name__)
app.config.update(DEBUG=True, SECRET_KEY=os.environ['SECRET_KEY'])
# перед запуском сервера, необходимо в консоле указать значение секретного ключа,
# например SECRET_KEY = secret

@app.route('/', methods=['GET', 'POST'])
def home():
    raise ValueError('Test!')
    return 'Hello World!', 200

if __name__ == '__main__':
    app.run()
