# Задание №6
# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
import argparse
import logging
import os
from collections import namedtuple

def parser():
    parser = argparse.ArgumentParser(description="Передается строка пути до католога")
    parser.add_argument("-p", type=str)
    arg = parser.parse_args()
    return arg.p


def show_info_derictory(path):
    my_format = '{levelname:<10} - {asctime:<10} - {msg}'
    logging.basicConfig(filename='show_info_derictory.log', format=my_format,
                        filemode='a', style='{',encoding='utf-8', level=logging.INFO)
    try:
        if os.path.isdir(path):
            parent_directory = os.path.basename(os.path.abspath(path))

        else:
            raise ValueError('Переданы некорректные значения!'
                             'Необходимо передать путь до директории на ПК.'
                             f'Вы передали {path}.')
    except ValueError as e:
        logging.error(e)
        return f'Программа завершила работу с ошибкой {e}'

    list_directory = []
    ObjectDerictory = namedtuple("ObjectDerictory", ["name", "extension", "flag_directory",
                                                     "parent_directory"])
    for file in os.listdir(path):
        if os.path.isdir(file):
            obj_file = ObjectDerictory(name=file, extension=False,
                                       flag_directory=True,
                                       parent_directory=parent_directory)
        else:
            name, extension = os.path.splitext(file)
            extension = extension[1:]
            obj_file = ObjectDerictory(name=name, extension=extension,
                                       flag_directory=False,
                                       parent_directory=parent_directory)
        list_directory.append(obj_file)
        logging.info(f'Название {"директории" if obj_file.flag_directory else "файла"}: {obj_file.name}'
                     f'{"." if not obj_file.flag_directory else " "}'
                     f'{obj_file.extension if not obj_file.flag_directory else ""} ||'
                     f'Родительский каталог: {obj_file.parent_directory}')
    return '\n'.join([f'Название {"директории" if obj_file.flag_directory else "файла"}: {obj_file.name}'
                 f'{"." if not obj_file.flag_directory else " "}'
                 f'{obj_file.extension if not obj_file.flag_directory else ""} ||'
                 f'Родительский каталог: {obj_file.parent_directory}' for obj_file in list_directory])


if __name__ == '__main__':
    print(show_info_derictory(parser()))

