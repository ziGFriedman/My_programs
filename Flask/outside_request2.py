from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    print(request)
    return ('Hello World!', 200)

# print(request, type(request), request.method) - случится ошибка т.к. реквест не
# определен в функции (он имеет контекст)

# with app.test_request_context('/?next=http://example.com/'):
#     print(request, type(request), request.method)

if __name__ == '__main__':
    app.run()
