# vowels = ['a', 'e' ,'i', 'o' , 'u']
# word = input("Provide a word to search for voweles: ")
# found = {}
#
# for letter in word:
#     if letter in vowels:
#         found.setdefault(letter, 0)
#         found[letter] += 1
#
# for k, v in sorted(found.items()):
#     print(k, 'was found', v, 'time(s). ')

#
# vowels = set ('aeiou') # union- объединяет два множвества -
# u = vowels.union(set(word))
# u_list = sorted(list(u))

# union объеденяет множества
# difference сообщает какие объекты присутсвтуют в одном, но отстутсвутют в другом множестве
# intersection - принимает объекты из одного множества и сравнивает их с объектами из другого, а затем
# сообщает об общих найденых объектах

vowels=set('aeiou')
word = input("Provide a word to search for vowels: ")
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)

    
