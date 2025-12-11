# app.py
from flask import Flask, render_template, request

app = Flask(__name__)


EDUCATION_LEVELS = [
    'Начальное',
    'Среднее',
    'Среднее специальное',
    'Высшее',
    'Ученая степень'
]

PROFESSIONS = [
    'Инженер-исследователь',
    'Пилот',
    'Строитель',
    'Экзобиолог',
    'Врач',
    'Инженер по терраформированию',
    'Климатолог',
    'Специалист по радиационной защите',
    'Астрогеолог',
    'Гляциолог',
    'Инженер жизнеобеспечения',
    'Метеоролог',
    'Оператор марсохода',
    'Киберинженер',
    'Штурман',
    'Пилот дронов'
]

GENDER_OPTIONS = ['Мужской', 'Женский']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        surname = request.form.get('surname')
        name = request.form.get('name')
        email = request.form.get('email')
        education = request.form.get('education')
        profession = request.form.get('profession')
        gender = request.form.get('gender')
        motivation = request.form.get('motivation')
        stay_on_mars = 'Да' if request.form.get('stay_on_mars') else 'Нет'


        return render_template('success.html',
                               surname=surname,
                               name=name,
                               email=email,
                               education=education,
                               profession=profession,
                               gender=gender,
                               motivation=motivation,
                               stay_on_mars=stay_on_mars)

    return render_template('form.html',
                           education_levels=EDUCATION_LEVELS,
                           professions=PROFESSIONS,
                           gender_options=GENDER_OPTIONS)


if __name__ == '__main__':
    app.run(debug=True)