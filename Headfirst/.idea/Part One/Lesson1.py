from datetime import datetime  # Импортирую из модуля datetime  субмоудль datetime

import time # Импорт субмодуля
import random # Импорт субмодуля

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37,
        39, 41, 43, 45, 47, 49, 51, 53, 55,
        57, 59] # Присваивание переменной

for i in range(5):  #  пишу повторения цилка значением range(x) раз
    right_this_minute = datetime.today().minute # этот вызов генерирует значение для присваивания переменной присваиваю переменную и импортирую функцию из субмодуля

    if right_this_minute in odds:  # условие если  текущая минута в переменной odds совпадает
        print("This minute seems a little odd.") # Если уловие верно, сделать вывод
    else:
        print("Not an odd minute.") # если условие ложно сделать вывод
wait_time=random.randint(1, 60)  # любое число от 1 до 60
time.sleep(wait_time)