word ="bottles"
for beer_num in range(99, 0, -1): #  есть ли beer_num в range от 99 до 0, при каждом вызове -1
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1: # если beer_num остался 1
        print("No more bottles of beer on the wall.") # то вывод истины
    else:
        new_num = beer_num -1 # отнимает -1 от  range ( 99, 0)
        if new_num == 1: # если равно 1
            word = "bottle"
        print(new_num, word, "of beer on the wall.") #  вывод количества бутылок после  beer_num -1
    print()