
#Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. \n
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''
a, b, c = ("один", "два", "три")

print(f'{a=} {b=} {c=}')

data = ("один", "два", "три", "четыре", "пять", "шесть", "семь")
a, b, *c, d = data
print(f"{a=}, {b=}, {c=}, {d=}")
'''

link = "alexanderzagaynov/Documents/DZ_01 seminar_advaced/DZ_05_seminar.py/DZ_01_task.py"

a, *b, c = link.split('/')
tuples_ = (a, b, c)
print(f' "1-Путь/way" - {link} \n\n "2-Имя файла/file_name" - {a=} \n\n "3-Раcширение/file_exstension" - {b=}')

print(f'"возвращаем кортеж: " {tuples_=}')

t = a, b, c  # ёще вариант создание кортежа
print(f'{t=}, {type(t)}')

