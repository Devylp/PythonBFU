from flask import Flask, url_for

# Создаем приложение Flask
app = Flask(__name__)


# Задание 1
@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


# Задание 2: Рекламная кампания (/promotion)
@app.route('/promotion')
def promotion():
    return """
    Человечество вырастает из детства.<br>
    Человечеству мала одна планета.<br>
    Мы сделаем обитаемыми безжизненные пока планеты.<br>
    И начнем с Марса!<br>
    Присоединяйся!
    """


# Задание 3: Картинка
@app.route('/mars')
def image_mars():
    # url_for('static', filename='mars.jpg') найдет файл в папке static
    image_url = url_for('static', filename='static/mars.jpg')

    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>

                    <img src="{image_url}" alt="Марс" style="width: 300px;">

                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


# Задание 4:
# Роут, который принимает 3 параметра из адресной строки: строку, целое и дробное число.
@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Результаты отбора</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендент {nickname}:</h2>

                    <p style="color: green;">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </p>
                    <h3>составляет {rating}!</h3>
                    <p style="color: orange;">
                      Желаем удачи!
                    </p>
                  </body>
                </html>"""



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')