from flask import Flask

app = Flask(__name__)    # Экземпляр класса Flask

@app.route('/')    # Декоратор маршрута URL
def home():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
