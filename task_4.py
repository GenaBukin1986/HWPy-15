# Задача 4. Опции и флаги
# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать, сколько раз повторить строку
import argparse

def function(number:int, string:str, verbose=None, repeat=None):
    if verbose:
        info = f"Число: {number}.\n" \
               f"Строка: {string}.\n" \
               f"Вывод дополнительной информации о процессе установелен.\n" \
               f"{f'Количество повторений строки: {repeat}' if repeat else ''}"
    if repeat:
        number_text = f"Повторяю строку {repeat} раз {', '.join([i for i in [string]*repeat])}"

    return f'Число: {number}.\n' \
           f'Строка: {string}.\n' \
           f'{info if verbose else number_text if repeat else ""}.\n' \
           f'{number_text}'


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(description="Передайте два аргумента: число и строку")
    my_parser.add_argument('--verbose', action="store_true", help="Вывод дополнительной информации")
    my_parser.add_argument('--repeat', type=int, default=1, help="Сколько раз повторить строку")
    my_parser.add_argument('-n', type=int, default=1)
    my_parser.add_argument('-t', type=str, default="Hello world")
    arg = my_parser.parse_args()

    print(function(arg.n, arg.t, arg.verbose, arg.repeat))