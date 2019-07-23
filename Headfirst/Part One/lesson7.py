vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found= {} # создаем пустой словарь
found['a']= 0 # инициализировать нулями значения ассоциированные с каждым из ключей
found['e']= 0
found['i']= 0
found['o']= 0
found['u']= 0
for letter in word:
    if letter in vowels:
        found[letter] += 1 # увелчить значение на единицу
for k, v in sorted(found.items() ): #  в цикле for используется метод items нужно определить две переменные k- ключей v- значений
    # вызвать метод items словаря found получить доступ к каждой записи  сданными во время операций
    print(k, 'was found', v, 'time(s).') # ключ и значений использвуется для вывода сообщений