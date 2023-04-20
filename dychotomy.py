import math  # нужен для вычисления тригонометрических функций
import pprint  # для адекватного вывода словаря с результатами


# Уравнение функции
def equation_func(x: int | float) -> float:
    result: float = math.sin(.3 - x) + .5 * (x - .1) ** 2
    return result


# Поиск точек перелома
def find_x_diff_change(x_val: list[float | int]) -> list[float | int]:
    x_close_zero: list[int | float] = []
    for i in range(len(x_val))[1:]:  # итерация со второго значения и до конца
        # Если рядом с точкой перелома есть f(x) = 0, то добавляется она вместо близкой к нулю
        if equation_func(x_val[i]) == 0:
            x_close_zero.append(x_val[i])
            continue
        elif equation_func(x_val[i-1]) == 0:    # чтобы точка f(x) = 0 не добавилась дважды
            continue
        # Если f(x) = 0 рядом нет, то добавляется точка, предшествующая пересечению оси x        
        if (equation_func(x_val[i]) <= 0) and (equation_func(x_val[i - 1]) >= 0):
            x_close_zero.append(x_val[i-1])
        elif (equation_func(x_val[i]) >= 0) and (equation_func(x_val[i - 1]) <= 0):
            x_close_zero.append(x_val[i-1])
    return x_close_zero


# Функция дихотомии
def dych(x_close_zero: list[int | float]) -> list[dict]:
    a: int | float
    b: int | float
    c: int | float

    eps: float = 10**-5  # заданная точность
    n: int  # счётчик шагов
    d: float  # ключевая переменная
    result: list[dict[str, int | float]] = []

    for x in x_close_zero:
        # Инициализация на нулевом шаге
        a = x
        b = a + .2
        c = (a + b) / 2
        n = 0
        d = b - a
        # "До тех пор, пока d не станет меньше или равно заданной точности"
        while d > eps:
            # Перерасчёт значений a, b и с в начале каждого шага
            if n != 0:
                if equation_func(a) * equation_func(c) < 0:
                    b = c
                else:
                    a = c
                c = (a + b) / 2

            d = b - a  # Самое важное вычисление в каждом шаге, зависит закончится цикл или нет
#               Если потребуется вывести список всех операций
#            print("n =", n, "\ta =", a, "\tb =", b, "\tc =", c, "\tf(a)*f(c) =",\
#                  equation_func(a) * equation_func(c), "\td =", d)
            n += 1
        else:
            n -= 1  # Сброс зря созданного шага (компенсация особенности работы while)
#        print("-" * 160)
        result.append({
            "a": a,
            "b": b,
            "c": c,
            "f(a)*f(c)": equation_func(a) * equation_func(c),
            "d": d
        })
    return result


# Создание листа значений x
x_values: list[float] = []
for i in range(-10, 32, 2):  # числа в 10 раз больше, т.к. range не принимает float
    x_values.append(i / 10)

x_close_zero = find_x_diff_change(x_values)  # Нахождение точек перегиба
dych_result = dych(x_close_zero)  # Запуск дихотомии по точкам перегиба
pprint.pprint(dych_result)
