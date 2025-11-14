'''
Задача 3

Напишите программу с графическим пользовательским интерфейсом на PyQT,
в которой в два текстовых поля вводятся целые числа. После нажатия кнопки
Рассчитать программа должна вычислить сумму, разность, частное и произведение
введённых чисел и вывести результат каждой операции в отдельные виджеты QLCDNumber.
В случае попытки деления на 0 программа должна выводить какое-либо сообщение.
'''

from PyQt6.QtWidgets import QApplication, QPushButton, QLineEdit, QMainWindow, QLabel, QLCDNumber


class Example(QMainWindow):
    def __init__(self, ):
        super().__init__()

        self.x_pos = 500
        self.y_pos = 500
        self.number_1 = 0
        self.number_2 = 0

        self.setGeometry(1920 // 2, 1080 // 2, self.x_pos, self.y_pos)
        self.setWindowTitle('Миникалькулятор')

        # Button
        self.button = QPushButton("->", self)
        self.button.resize(50, 50)
        self.button.move(225, 150)

        # Labels
        self.label1 = QLabel(self)
        self.label1.setText("Первое число (целое):")
        self.label1.resize(175, 25)
        self.label1.move(75, 100)

        self.label2 = QLabel(self)
        self.label2.setText("Второе число (целое):")
        self.label2.resize(175, 25)
        self.label2.move(75, 160)

        self.label3 = QLabel(self)
        self.label3.setText("Сумма:")
        self.label3.move(350, 100)

        self.label4 = QLabel(self)
        self.label4.setText("Разность:")
        self.label4.move(350, 160)

        self.label5 = QLabel(self)
        self.label5.setText("Произведение:")
        self.label5.move(350, 220)

        self.label6 = QLabel(self)
        self.label6.setText("Частное:")
        self.label6.move(350, 280)

        # Forms
        self.input_form1 = QLineEdit(self)
        self.input_form1.resize(75, 25)
        self.input_form1.move(75, 130)

        self.input_form2 = QLineEdit(self)
        self.input_form2.resize(75, 25)
        self.input_form2.move(75, 190)

        # LCD
        self.LCD_count_add = QLCDNumber(self)
        self.LCD_count_add.resize(75, 25)
        self.LCD_count_add.move(350, 130)

        self.LCD_count_sub = QLCDNumber(self)
        self.LCD_count_sub.resize(75, 25)
        self.LCD_count_sub.move(350, 190)

        self.LCD_count_mul = QLCDNumber(self)
        self.LCD_count_mul.resize(75, 25)
        self.LCD_count_mul.move(350, 250)

        self.LCD_count_div = QLCDNumber(self)
        self.LCD_count_div.resize(75, 25)
        self.LCD_count_div.move(350, 310)

        self.button.clicked.connect(self.evaluation)

    def evaluation(self):
        self.number_1 = int(self.input_form1.text())
        self.number_2 = int(self.input_form2.text())

        # Сумма операнды
        self.LCD_count_add.display(self.number_1 + self.number_2)

        # Разность операндов
        self.LCD_count_sub.display(self.number_1 - self.number_2)

        # Произведение операндов
        self.LCD_count_mul.display(self.number_1 * self.number_2)

        # Частное операндов
        if self.number_2 != 0:
            self.LCD_count_div.display(self.number_1 / self.number_2)

        else:
            self.LCD_count_div.display("Error")


app = QApplication([])

ex = Example()
ex.show()

app.exec()
