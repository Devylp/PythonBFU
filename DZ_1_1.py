'''
Задача 1

Напишите перекидыватель слов. На форме разместите два поля для ввода и кнопку.
На кнопке должна быть показана стрелка от первого поля ко второму.
В первое поле вводится строчка, и по нажатию кнопки эта строчка перебрасывается в другое поле,
при этом стрелка на кнопке меняется на противоположную. При повторном нажатии строчка летит обратно,
а стрелка на кнопке меняется на изначальную. И так далее.
'''

from PyQt6.QtWidgets import QApplication, QPushButton, QLineEdit, QMainWindow


class Example(QMainWindow):
    def __init__(self, ):
        super().__init__()

        x_pos = 300
        y_pos = 200
        self.is_moving_right = True

        self.setGeometry(1920//2, 1080//2, x_pos, y_pos)
        self.setWindowTitle('Фокус со словами')

        self.btn = QPushButton('->', self)
        self.btn.resize(25, 25)
        self.btn.move(80, 80)

        # First form
        self.name_input1 = QLineEdit(self)
        self.name_input1.resize(75, 25)
        self.name_input1.move(0, 80)
        self.name_input1.setText("Фокус")

        # Second form
        self.name_input2 = QLineEdit(self)
        self.name_input2.resize(75, 25)
        self.name_input2.move(110, 80)

        self.btn.clicked.connect(self.magick)

    def magick(self):
        if self.is_moving_right:
            text_to_move = self.name_input1.text()

            self.name_input2.setText(text_to_move)
            self.name_input1.clear()
            self.btn.setText('<-')
            self.is_moving_right = False
        else:
            text_to_move = self.name_input2.text()

            self.name_input1.setText(text_to_move)
            self.name_input2.clear()
            self.btn.setText('->')
            self.is_moving_right = True





app = QApplication([])

ex = Example()
ex.show()

app.exec()
