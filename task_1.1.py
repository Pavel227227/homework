# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# Решение
len(my_favorite_songs)
print('Первый трек -', my_favorite_songs[0:14])
print('Последний -', my_favorite_songs[-13:])
print('Второй -', my_favorite_songs[16:30])
print('Второй с конца -', my_favorite_songs[-26:-15])