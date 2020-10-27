# Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
import os

min_num = 1
max_num = 10


def make_dirs():
    for new_dir_i in range(min_num, max_num):
        new_dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(new_dir_i))
        os.mkdir(new_dir_path)


def remove_dirs():
    for i in range(min_num, max_num):
        path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.rmdir(path)


if __name__ == "__main__":
    make_dirs()
    remove_dirs()
