# Задача 3. Планирование задач
# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD
from datetime import timedelta, datetime

def function(day: int):
    try:
        if day < 0:
            raise ValueError("Не возможно запланировать мероприятия в прошлом")
    except ValueError as e:
        return f"Возникла ошибка! {e}"
    current_day = datetime.now()
    delta = timedelta(days=day)
    return (current_day + delta).strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(function(-1))