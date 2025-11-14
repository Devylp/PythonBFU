'''
Задача 2

Напишите программу с графическим пользовательским интерфейсом на PyQT.
В однострочное поле вводится корректное арифметическое выражение, которое можно вычислить без ошибок.
По кнопке Вычислить надо посчитать результат этого выражения и вывести его в другое поле для ввода.
Чтобы вычислить любое выражение, заданное в строке, можно использовать функцию eval().
'''

from PyQt6.QtWidgets import QApplication, QPushButton, QLineEdit, QMainWindow, QLabel

class Example(QMainWindow):
    def __init__(self, ):
        super().__init__()

        self.x_pos = 350
        self.y_pos = 350
        self.is_in_expression = True
        self.result = None

        self.setGeometry(1920//2, 1080//2, self.x_pos, self.y_pos)
        self.setWindowTitle('Вычисление выражении')

        # Button
        self.button = QPushButton("->", self)
        self.button.resize(25, 25)
        self.button.move(120, 60)

        # Labels
        self.label = QLabel(self)
        self.label.setText("Выражение:")
        self.label.move(40, 30)

        self.name_label = QLabel(self)
        self.name_label.setText("Результат:")
        self.name_label.move(150, 30)

        # Forms
        self.input_form = QLineEdit(self)
        self.input_form.resize(75, 25)
        self.input_form.move(40, 60)

        self.output_form = QLineEdit(self)
        self.output_form.resize(75, 25)
        self.output_form.move(150, 60)

        self.button.clicked.connect(self.evaluation)

    
    def evaluation(self):
        self.result = str(eval(self.input_form.text()))
        self.output_form.setText(self.result)
        self.input_form.clear()




app = QApplication([])

ex = Example()
ex.show()

app.exec()
