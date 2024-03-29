from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def start():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
   pass


@app.route('/promotion')
def promotion():
    list_prom = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                 'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                 'Присоединяйся!'
                 ]

    return '<br/>'.join(list_prom)


@app.route('/image_mars')
def mars():
    pass


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
