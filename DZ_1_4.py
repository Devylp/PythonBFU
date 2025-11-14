'''
Задача 4

Напишите программу Заказ в McDonald’s с графическим пользовательским интерфейсом на PyQT.
Пользователь должен иметь возможность выбирать одно или несколько блюд.
После нажатия на кнопку Заказать в отдельном виджете должен отображаться «чек» с выбранными позициями.
В качестве виджета для вывода информации о заказе можете использовать виджет QPlainTextEdit.
'''

from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QPlainTextEdit, QCheckBox, QLabel


class Example(QMainWindow):
    def __init__(self, ):
        super().__init__()

        self.x_pos = 700
        self.y_pos = 500
        self.order_list = []
        self.output_text = "Пока заказ не сделан."

        self.setGeometry(1920//2, 1080//2, self.x_pos, self.y_pos)
        self.setWindowTitle('Заказ в McDonald’s')

        # Button
        self.button = QPushButton('Заказать', self)
        self.button.resize(100, 25)
        self.button.move(50, 150)

        # Labels
        self.label_chs = QLabel(self)
        self.label_chs.setText("Чизбургер")
        self.label_chs.resize(100, 20)
        self.label_chs.move(75, 50)

        self.label_gmb = QLabel(self)
        self.label_gmb.setText("Гамбургер")
        self.label_gmb.resize(100, 20)
        self.label_gmb.move(75, 70)

        self.label_nug = QLabel(self)
        self.label_nug.setText("Нагетсы")
        self.label_nug.resize(100, 20)
        self.label_nug.move(75, 90)

        self.label_cola = QLabel(self)
        self.label_cola.setText("Кока-кола")
        self.label_cola.resize(100, 20)
        self.label_cola.move(75, 110)

        # Checkbox
        self.check_box_chs = QCheckBox(self)
        self.check_box_chs.resize(20, 20)
        self.check_box_chs.move(50, 50)

        self.check_box_gmb = QCheckBox(self)
        self.check_box_gmb.resize(20, 20)
        self.check_box_gmb.move(50, 70)

        self.check_box_nug = QCheckBox(self)
        self.check_box_nug.resize(20, 20)
        self.check_box_nug.move(50, 90)

        self.check_box_cola = QCheckBox(self)
        self.check_box_cola.resize(20, 20)
        self.check_box_cola.move(50, 110)

        # Order output window
        self.order_output_window = QPlainTextEdit(self)
        self.order_output_window.setFixedSize(250, 250)
        self.order_output_window.setPlainText(self.output_text)
        self.order_output_window.move(50, 190)

        self.order_status = {
            self.check_box_chs: "Чизбургер",
            self.check_box_gmb: "Гамбургер",
            self.check_box_nug: "Нагетсы",
            self.check_box_cola: "Кока-кола"
        }

        self.button.clicked.connect(self.output_order)

    def output_order(self):
        self.order_list = []

        for key in self.order_status:
            if key.isChecked():
                self.order_list.append(self.order_status[key])

        if self.order_list:
            self.output_text = "Ваш заказ:\n\n" + "\n".join(self.order_list)
        else:
            self.output_text = "Вы ничего не выбрали."

        self.order_output_window.setPlainText(self.output_text)



app = QApplication([])

ex = Example()
ex.show()

app.exec()
