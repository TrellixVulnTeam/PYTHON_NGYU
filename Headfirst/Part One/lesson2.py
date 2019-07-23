from datetime import datetime # Импортирую из модуля datetime  субмоудль datetime


today = datetime.today()  # Присваиваю today()
condition = datetime.today().day # today().day

if today == 'Saturday':  # если день Saturday
    print('Party!') # вывод истины
elif today == 'Sunday': # или если sunday
    if condition == 'Headache':
        print('Recover, then rest.')
    else:
        print('Rest.')
else:
    print('Work, Work, Work') # вывод если условие ложно