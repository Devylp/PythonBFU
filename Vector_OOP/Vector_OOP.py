from math import sqrt


class Vector3D:
    coordinates = []

    # Констркутор
    def __init__(self, x=0, y=0, z=0):
        self.coordinates = [x, y, z]
        self.x = x
        self.y = y

    # Сложение векторов (переопределение оператора +)
    def __add__(self, other):
        new_x = self.coordinates[0] + other.coordinates[0]
        new_y = self.coordinates[1] + other.coordinates[1]
        new_z = self.coordinates[2] + other.coordinates[2]

        return Vector3D(new_x, new_y, new_z)

    # Вычитание векторов (переопределение оператора -)
    def __sub__(self, other):
        new_x = self.coordinates[0] - other.coordinates[0]
        new_y = self.coordinates[1] - other.coordinates[1]
        new_z = self.coordinates[2] - other.coordinates[2]

        return Vector3D(new_x, new_y, new_z)

    # Модуль вектора (длина)
    def __abs__(self):
        return sqrt(
            self.coordinates[0] ** 2
            + self.coordinates[1] ** 2
            + self.coordinates[2] ** 2
        )

    # Унарный минус
    def unary_minus(self):
        self.coordinates[0] *= -1
        self.coordinates[1] *= -1
        self.coordinates[2] *= -1

        return self

    # Скалярное произведение и умножение на скаляр
    def __mul__(self, other):
        # Скалярное произведение
        if isinstance(other, Vector3D):
            prod_x = self.coordinates[0] * other.coordinates[0]
            prod_y = self.coordinates[1] * other.coordinates[1]
            prod_z = self.coordinates[2] * other.coordinates[2]

            return prod_x + prod_y + prod_z

        # Ветка с умножением на скаляр
        elif isinstance(other, int):
            self.coordinates[0] *= other
            self.coordinates[1] *= other
            self.coordinates[2] *= other

            return self

        # Обработка неподдерживаемых типов
        else:
            return NotImplemented

    # Векторное произведение
    def vector_product(self, other):
        i = Vector3D(1, 0, 0)
        j = Vector3D(0, 1, 0)
        k = Vector3D(0, 0, 1)

        vec_x = (
            self.coordinates[1] * other.coordinates[2]
            - self.coordinates[2] * other.coordinates[1]
        )
        vec_y = (
            self.coordinates[0] * other.coordinates[2]
            - self.coordinates[2] * other.coordinates[0]
        )
        vec_z = (
            self.coordinates[0] * other.coordinates[1]
            - self.coordinates[1] * other.coordinates[0]
        )
        result = Vector3D()
        result = i * vec_x - j * vec_y + k * vec_z
        return result

    # Получить элемент вектора
    def __getitem__(self, item):
        return self.coordinates[item]

    # Установить элемент вектора
    def __setitem__(self, key, value):
        self.coordinates[key] = value

    # Вывод вектора
    def __str__(self):
        return str(self.coordinates)


vector1 = Vector3D(1, 2, 3)

print(vector1)
