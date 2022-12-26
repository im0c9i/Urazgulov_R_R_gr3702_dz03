# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
#  и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 10.01]


def array(my_list):
    max = 0
    min = 1
    for i in my_list:
        temp = round(i % 1, 3)
        if temp > max:
            max = temp
        elif temp < min:
            min = temp
    print(f'maximum {max}, minimum {min}')
    result = max - min
    return result

print(array(my_list))

