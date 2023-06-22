
def switch_it_up(number):
    words = {
        0: 'Ноль',
        1: 'Один',
        2: 'Два',
        3: 'Три',
        4: 'Четыре',
        5: 'Пять',
        6: 'Шесть',
        7: 'Семь',
        8: 'Восемь',
        9: 'Девять',
        10: 'Десять',
    }
    return words.get(number)
n = int(input('Введите число:'))
print(switch_it_up(n))