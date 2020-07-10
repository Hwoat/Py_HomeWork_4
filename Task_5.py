'''
Реализовать формирование списка, используя
функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000
(включая границы). Необходимо получить результат
вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

from functools import reduce


def my_func(element_p, element):
    return element_p * element

print(f'Список четных значений {[element for element in range(99, 1001) if element % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [element for element in range(99, 1001) if element % 2 == 0])}')