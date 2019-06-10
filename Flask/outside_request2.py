from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return ('Hello World!', 200)

print(request, type(request), request.method)

if __name__ == '__main__':
    app.run()
