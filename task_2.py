# Задача 2. Работа с текущим временем и датой
# Напишите скрипт, который получает текущее время и дату,
# а затем выводит их в формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер недели в году.
from datetime import datetime


def function():
    current_date = datetime.now()
    return '\n'.join([i for i in [f"Текущая дата: {current_date.strftime('%Y-%m-%d %H:%M:%S')}",
                                  f"День недели: {current_date.strftime('%A')}",
                                  f"Номер недели в году: {current_date.isocalendar().week}"]])


if __name__ == '__main__':
    print(function())
