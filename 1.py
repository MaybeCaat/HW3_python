# создаём функцию cat_eat, которая принимает 2 кортежа horse_coord и figure_coord,
# в которых хранятся положение коня и фигуры соответственно
def can_eat(horse_coord, figure_coord):
    # в переменную difference_x посчитаем расстояние между конём и фигурой по оси x
    # так как расстояние не может быть отрицательным, а разница координат может -
    # используем функцию для модуля abs()
    difference_x = abs(horse_coord[0] - figure_coord[0])
    # в переменную difference_y посчитаем расстояние между конём и фигурой по оси y
    difference_y = abs(horse_coord[1] - figure_coord[1])
    # конь ходит на 2 клетки по одной оси и на 1 по другой, соответственно
    # конь может съесть фигуру, если она стоит на расстоянии 2 оси x и на расстоянии 1 по оси y
    # (расстояния у нас записаны в переменных difference_x и difference_y) или наоборот
    # если условие на расстояние сошлось, ...
    if (difference_x == 2 and difference_y == 1) or (difference_x == 1 and difference_y == 2):
        # то выводим True, конь может съесть
        return True
    # условие не выполнилось, а значит конь не может за 1 ход съесть фигуру, ...
    else:
        # поэтому возвращаем False
        return False
