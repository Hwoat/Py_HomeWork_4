'''
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
'''

from itertools import count
i = int(input('Введите стартовое число '))
x = i
for element in count(i):
    if x == i + 20:
        break
    print(element)
    x += 1

from itertools import cycle
y = 1

my_list = [True, 'Donatello', 1488, None]
for element in cycle(my_list):
    if y > 20:
        break
    print(element)
    y += 1

# ОГРАНИЧИЛ БЕСКОНЕЧНЫЙ ЦИКЛ. ИНАЧЕЛ ЛЫЛ РИСК "ПОВЕСИТЬ" СИСТЕМУ! )

