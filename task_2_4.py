# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"


# Решение пункт А:

# s = "Hi! Hello!"
# def remove_exclamation_marks(s):
#     return s.replace('!', '')
# print(remove_exclamation_marks(s))



# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"


# Решение пункт В.
# s = 'Hi!!!!'
# def remove_last_em(s):
#     if s.endswith("!"):
#         return s[:-1]
#     else:
#         return s
# print(remove_last_em(s))


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"


s = 'Hi!, Hi'
def remove(s): 
 return ' '.join(w for w in s.split() if w.count('!') != 1)
print(remove(s))
