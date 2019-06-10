from flask import Flask
from flask import request
# pip install flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=25)
        ])    # ожидает в форме значения по названию переменных
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35),
        validators.Email()    # правильность записи емайла
        ])
# Можно валидировать множество форм
    job = StringField(validators=[
        validators.Length(min=0, max=4),
        validators.Required()    # указывает поле, обязательное для заполнения
        ])

app = Flask(__name__)
app.config.update(DEBUG=True, SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False)
# app.config.update(DEBUG=True) перезапускает сервер при изменении кода (режим отладки)

# форма обязательно наследуется от класса с параметром FlaskFrom
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)    # print - передает значения в консоль
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)    # return - передает значения на страничку
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return ('hello world!', 200)

if __name__ == '__main__':
    app.run()
