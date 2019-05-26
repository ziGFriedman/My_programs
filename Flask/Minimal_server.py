'''Flast - реализация контроллера (app)'''

from flask import Flask

app = Flask(__name__)    # Экземпляр класса Flask

@app.route('/')    # Декоратор маршрута URL
def home():
    return 'Hello World!'    # View

if __name__ == '__main__':
    app.run()

'''             Routes
                  |
    Model <--> Controller --> View --> Desktop
      |
   Database  '''

'''Во Flask используется Model View Controller (MVC)
Она представляет собой одну из реализаций парадигмы "разделение ответственности"
Может использоваться только в приложениях, где существует UI'''

'''Маршруты (Routes) устанавливает соответствие между URL адресом и функцией вида View'''

'''Controller - получает запрос Request от пользователя, выбирает какой маршрут Rout ему
соответствует, оперирует выборкой данных, вызывает нужную функцию вида View'''

'''View - используется для отображения данных Model'''

'''Model - используется для представления данных и для изменения данных'''

'''Web Server Gateway Interface (WSGI)
Используется для общения Python-программы и сервера (Uginx, Apache)
Используется всеми Web-фреймворками для Python'''

'''Werkzeug - библиотека, которая работает с WSGI, лежит в основе Flask'''
