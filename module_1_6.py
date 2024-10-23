my_dict = {'Альберт': 1986, 'Руслан': 1988, 'Максим': 1906} # словарь
print(my_dict)
print(my_dict.get('Руслан')) # метод возвращает значение по ключу
print(my_dict.get('Кристина')) # метод возвращает значение по ключу
my_dict.update({'Мария': 1987,
                'Андрей': 1985}) # метод добавления в словарь нескольких значений
a = my_dict.pop('Альберт') # удаление из словаря по ключу
print(a)
print(my_dict)

my_set = {1, 1, 3, 5, 5, 'Stol', 'Stol'} # множество
print(my_set)
my_set.update({(1, 2, 3,), # добавление элементов в множество
              29.353})
my_set.discard(1) # удаление элемента из множества
print(my_set)